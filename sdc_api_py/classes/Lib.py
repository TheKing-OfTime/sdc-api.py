import asyncio
import aiohttp


class Querier:
    """
    Объект для последовательного выполнения запросов с кулдауном.
    На данный момент, кулдаун составляет 2 секунды (ограничение API)
    """
    RATELIMIT_DEFAULT_SECONDS:  int = 2
    RATELIMIT_BOTS_SECONDS:  int = 30
    query_lock:         asyncio.Lock = asyncio.Lock()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Querier, cls).__new__(cls)
        return cls.instance

    async def execute_get_query(self, *args, **kwargs):
        await self.query_lock.acquire()
        response = None

        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get(*args, **kwargs)
                if int(response.status) != 200:
                    print(f"SDC Произошла ошибка: {response.status} {response.json()}")
        finally:
            asyncio.get_event_loop().create_task(self._wait_ratelimit())

        return response

    async def execute_post_query(self, *args, **kwargs):
        await self.query_lock.acquire()
        response = None

        try:
            async with aiohttp.ClientSession() as session:
                response = await session.post(*args, **kwargs)
                if int(response.status) != 200:
                    print(f"SDC Произошла ошибка: {response.status} {response.json()}")
        finally:
            asyncio.get_event_loop().create_task(self._wait_ratelimit("bots"))

        return response

    async def _wait_ratelimit(self, execution_type:str = "default"):
        if execution_type == "default":
            await asyncio.sleep(self.RATELIMIT_DEFAULT_SECONDS)
        elif execution_type == "bots":
            await asyncio.sleep(self.RATELIMIT_BOTS_SECONDS)
        self.query_lock.release()
