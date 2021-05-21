import asyncio
import aiohttp


class Querier:
    """
    Объект для последовательного выполнения запросов с кулдауном.
    На данный момент, кулдаун составляет 2 секунды (ограничение API)
    """
    RATELIMIT_SECONDS: int = 2
    query_lock: asyncio.Lock = asyncio.Lock()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Querier, cls).__new__(cls)
        return cls.instance

    async def execute_get_query(self, *args, **kwargs):
        return await self._execute_query("get", *args, **kwargs)

    async def execute_post_query(self, *args, **kwargs):
        return await self._execute_query("post", *args, **kwargs)

    async def _execute_query(self, method, *args, **kwargs):
        await self.query_lock.acquire()
        data = None

        try:
            async with aiohttp.ClientSession() as session:
                query_types = {
                    "get": session.get,
                    "post": session.post,
                }

                response = await query_types[method](*args, **kwargs)
                data = await response.json()
        except Exception as e:
            # Unlock mutex without ratelimiting and rase exception
            self.query_lock.release()
            raise
        else:
            asyncio.create_task(self._wait_ratelimit())

        # Error handling
        if data["error"] is not None:
            raise SdcAPIException(**(data["error"]))

        return data

    async def _wait_ratelimit(self):
        await asyncio.sleep(self.RATELIMIT_SECONDS)
        self.query_lock.release()


class SdcAPIException(Exception):
    """
    Класс ошибок, возвращаемых API
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        if hasattr(self, 'message'):
            return f"При выполнении запроса к API возникла ошибка: {self.message}"
        else:
            return "При выполнении запроса к API возникла неизвестная ошибка"
