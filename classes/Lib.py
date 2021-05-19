import asyncio
import aiohttp

class Querier:
    """
    Объект для последовательного выполнения запросов с кулдауном.
    На данный момент, кулдаун составляет 2 секунды (ограничение API)
    """
    RATELIMIT_SECONDS: int = 2

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Querier, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.query_lock = asyncio.Lock()

    async def execute_get_query(self, *args, **kwargs):
        await self.query_lock.acquire()
        response = None

        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get(*args, **kwargs)
        finally:
            asyncio.get_event_loop().create_task(self._wait_ratelimit())

        return response

    async def execute_post_query(self, *args, **kwargs):
        await self.query_lock.acquire()
        response = None

        try:
            async with aiohttp.ClientSession() as session:
                response = await session.post(*args, **kwargs)
        finally:
            asyncio.get_event_loop().create_task(self._wait_ratelimit())

        return response

    async def _wait_ratelimit(self):
        await asyncio.sleep(self.RATELIMIT_SECONDS)
        await self.query_lock.release()
