from .. import _types
import time
from .Lib import Querier


class NikaWarns:

    def __init__(self, token):
        self.SDC_token = token
        self.querier = Querier()

    async def fetch_warns(self, _id):
        _id = int(_id)

        response = await self.querier.execute_get_query(
            f"https://api.server-discord.com/v2/warns/{_id}",
            headers={"Authorization": f"SDC {self.SDC_token}"}
        )

        data = await response.json()

        SdcNikaWarns = _types.SdcRawNikaWarns()

        SdcNikaWarns.id     = data["id"]
        SdcNikaWarns.type   = data["type"]
        SdcNikaWarns.warns  = data["warns"]

        return SdcNikaWarns
