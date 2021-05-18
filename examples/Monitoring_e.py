import asyncio
from classes.Monitoring import Monitoring

Sdc = Monitoring("")


async def test():
    response = await Sdc.get_guild(433242520034738186)
    print(response.status.youtube, response.status.sitedev)

asyncio.run(test())
