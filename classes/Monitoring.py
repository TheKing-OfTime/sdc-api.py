import aiohttp

import _types


def convert_to_SdcGuildStatus(Raw: _types.SdcRawGuildStatus):
    SdcGuildStatus = _types.SdcGuildStatus
    SdcGuildStatus.raw = Raw

    SdcGuildStatus.sitedev      = bool(Raw.status & 1)
    SdcGuildStatus.verified     = bool(Raw.status & 2)
    SdcGuildStatus.partner      = bool(Raw.status & 4)
    SdcGuildStatus.favorite     = bool(Raw.status & 8)
    SdcGuildStatus.bughunter    = bool(Raw.status & 16)
    SdcGuildStatus.easteregg    = bool(Raw.status & 32)
    SdcGuildStatus.botdev       = bool(Raw.status & 64)
    SdcGuildStatus.youtube      = bool(Raw.status & 128)
    SdcGuildStatus.twitch       = bool(Raw.status & 256)
    SdcGuildStatus.spamhunt     = bool(Raw.status & 512)

    return SdcGuildStatus


class Monitoring:
    def __init__(self, token: str):
        self.SDC_token = token

    async def fetch_guild_raw(self, _id: int):
        _id = int(_id)

        async with aiohttp.ClientSession() as session:
            response = await session.get(
                f"https://api.server-discord.com/v2/guild/{_id}",
                headers={"Authorization": f"SDC {self.SDC_token}"})

        data = await response.json()
        print(data)

        SdcRawGuildStatus           = _types.SdcRawGuildStatus
        SdcRawGuildStatus.status    = data["status"]

        SdcRawGuild             = _types.SdcRawGuild
        SdcRawGuild.avatar      = data["avatar"]
        SdcRawGuild.lang        = data["lang"]
        SdcRawGuild.name        = data["name"]
        SdcRawGuild.description = data["des"]
        SdcRawGuild.invite      = data["invite"]
        SdcRawGuild.owner       = data["owner"]
        SdcRawGuild.online      = data["online"]
        SdcRawGuild.members     = data["members"]
        SdcRawGuild.bot         = data["bot"]
        SdcRawGuild.boost       = data["boost"]
        SdcRawGuild.status      = SdcRawGuildStatus
        SdcRawGuild.upCount     = data["upCount"]
        SdcRawGuild.tags        = data["tags"]

        return SdcRawGuild

    async def get_guild(self, _id: int):
        _id = int(_id)

        Raw = await self.fetch_guild_raw(_id)

        SdcGuild                = _types.SdcGuild
        SdcGuild.avatar         = Raw.avatar
        SdcGuild.lang           = Raw.lang
        SdcGuild.name           = Raw.name
        SdcGuild.description    = Raw.description
        SdcGuild.invite         = Raw.invite
        SdcGuild.owner          = Raw.owner
        SdcGuild.online         = Raw.online
        SdcGuild.members        = Raw.members
        SdcGuild.bot            = True if Raw.bot else False
        SdcGuild.boost          = Raw.boost
        SdcGuild.status         = convert_to_SdcGuildStatus(Raw.status)
        SdcGuild.upCount        = Raw.upCount
        SdcGuild.tags           = Raw.tags.split(",")
        SdcGuild.id             = _id

        return SdcGuild
