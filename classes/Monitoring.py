import sdc_api._types as _types
import time
from sdc_api.classes.Lib import Querier


def convert_to_SdcGuildStatus(raw: _types.SdcRawGuildStatus):
    SdcGuildStatus = _types.SdcGuildStatus
    SdcGuildStatus.raw = raw

    SdcGuildStatus.sitedev = bool(raw.status & 1)
    SdcGuildStatus.verified = bool(raw.status & 2)
    SdcGuildStatus.partner = bool(raw.status & 4)
    SdcGuildStatus.favorite = bool(raw.status & 8)
    SdcGuildStatus.bughunter = bool(raw.status & 16)
    SdcGuildStatus.easteregg = bool(raw.status & 32)
    SdcGuildStatus.botdev = bool(raw.status & 64)
    SdcGuildStatus.youtube = bool(raw.status & 128)
    SdcGuildStatus.twitch = bool(raw.status & 256)
    SdcGuildStatus.spamhunt = bool(raw.status & 512)

    return SdcGuildStatus


class Monitoring:
    def __init__(self, token: str):
        self.SDC_token = token
        self.querier = Querier()

    async def fetch_guild_raw(self, _id: int):
        _id = int(_id)

        response = await self.querier.execute_get_query(
            f"https://api.server-discord.com/v2/guild/{_id}",
            headers={"Authorization": f"SDC {self.SDC_token}"}
        )

        data = await response.json()

        SdcRawGuildStatus = _types.SdcRawGuildStatus
        SdcRawGuildStatus.status = data["status"]

        SdcRawGuild = _types.SdcRawGuild
        SdcRawGuild.avatar = data["avatar"]
        SdcRawGuild.lang = data["lang"]
        SdcRawGuild.name = data["name"]
        SdcRawGuild.description = data["des"]
        SdcRawGuild.invite = data["invite"]
        SdcRawGuild.owner = data["owner"]
        SdcRawGuild.online = data["online"]
        SdcRawGuild.members = data["members"]
        SdcRawGuild.bot = data["bot"]
        SdcRawGuild.boost = data["boost"]
        SdcRawGuild.status = SdcRawGuildStatus
        SdcRawGuild.upCount = data["upCount"]
        SdcRawGuild.tags = data["tags"]

        return SdcRawGuild

    async def get_guild(self, _id: int):
        _id = int(_id)

        Raw = await self.fetch_guild_raw(_id)
        extension = "gif" if Raw.avatar.startswith("a_") else "png"

        SdcGuild = _types.SdcGuild
        SdcGuild.avatar = f"https://cdn.discordapp.com/icons/{_id}/{Raw.avatar}.{extension}"
        SdcGuild.lang = Raw.lang
        SdcGuild.name = Raw.name
        SdcGuild.description = Raw.description
        SdcGuild.invite = Raw.invite
        SdcGuild.owner = Raw.owner
        SdcGuild.online = Raw.online
        SdcGuild.members = Raw.members
        SdcGuild.bot = bool(Raw.bot)
        SdcGuild.boost = Raw.boost
        SdcGuild.status = convert_to_SdcGuildStatus(Raw.status)
        SdcGuild.upCount = Raw.upCount
        SdcGuild.tags = Raw.tags.split(",")
        SdcGuild.id = _id

        return SdcGuild

    async def fetch_guild_place(self, _id: int):
        _id = int(_id)

        response = await self.querier.execute_get_query(
            f"https://api.server-discord.com/v2/guild/{_id}/place",
            headers={"Authorization": f"SDC {self.SDC_token}"}
        )

        data = await response.json()

        SdcGuildPlace = _types.SdcGuildPlace

        SdcGuildPlace.place = data["place"]

        return SdcGuildPlace

    async def fetch_guild_rate_raw(self, _id: int):
        _id = int(_id)

        response = await self.querier.execute_get_query(
            f"https://api.server-discord.com/v2/guild/{_id}/rated",
            headers={"Authorization": f"SDC {self.SDC_token}"}
        )

        data = await response.json()

        SdcRawGuildRates = _types.SdcRawGuildRates

        SdcRawGuildRates.rates = data

        return SdcRawGuildRates

    async def get_guild_rate(self, _id):
        _id = int(_id)

        raw = await self.fetch_guild_rate_raw(_id)
        SdcGuildRates = _types.SdcGuildRates
        plus = []
        minus = []

        for item in raw.rates.items():
            if item[1] == 1:
                plus.append(item[0])
            if item[1] == -1:
                minus.append(item[0])

        SdcGuildRates.plus = plus
        SdcGuildRates.minus = minus
        SdcGuildRates.plus_count = len(plus)
        SdcGuildRates.minus_count = len(minus)

        return SdcGuildRates

    async def fetch_user_rate_raw(self, _id: int):
        _id = int(_id)

        response = await self.querier.execute_get_query(
            f"https://api.server-discord.com/v2/guild/{_id}/rated",
            headers={"Authorization": f"SDC {self.SDC_token}"}
        )

        data = await response.json()

        SdcRawUserRates = _types.SdcRawUserRates

        SdcRawUserRates.rates = data

        return SdcRawUserRates

    async def get_user_rate(self, _id):
        _id = int(_id)

        raw = await self.fetch_user_rate_raw(_id)
        SdcUserRates = _types.SdcUserRates
        plus = []
        minus = []

        for item in raw.rates.items():
            if item[1] == 1:
                plus.append(item[0])
            if item[1] == -1:
                minus.append(item[0])

        SdcUserRates.plus = plus
        SdcUserRates.minus = minus
        SdcUserRates.plus_count = len(plus)
        SdcUserRates.minus_count = len(minus)

        return SdcUserRates
