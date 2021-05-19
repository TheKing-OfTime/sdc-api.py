import aiohttp
import sdc_api._types as _types
import time
from sdc_api.classes.Lib import RateLimits as RL


class NikaWarns:

    def __init__(self, token):
        self.SDC_token = token

    async def fetch_warns(self, _id):
        _id = int(_id)
        if time.time() - RL.LASTREQUEST > RL.DEFAULT:
            RL.LASTREQUEST = time.time()
            async with aiohttp.ClientSession() as session:
                response = await session.get(
                    f"https://api.server-discord.com/v2/warns/{_id}",
                    headers={"Authorization": f"SDC {self.SDC_token}"})

            data = await response.json()

            SdcNikaWarns = _types.SdcRawNikaWarns

            SdcNikaWarns.id     = data["id"]
            SdcNikaWarns.type   = data["type"]
            SdcNikaWarns.warns  = data["warns"]

            return SdcNikaWarns
        else:
            raise RuntimeError("Слишком частые запросы.\nСтандартный лимит: 2 секунды")
