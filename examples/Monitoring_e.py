import asyncio
from classes.Monitoring import Monitoring

Sdc = Monitoring("")


async def test():
    response = await Sdc.get_user_rate(500020124515041283)
    print(response.plus_count, response.minus_count)

asyncio.run(test())
