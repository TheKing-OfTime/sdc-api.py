from dataclasses import dataclass, field
from .Raw import SdcRawGuildStatus


@dataclass
class SdcGuildStatus:
    """
    Тип данных хранящий обработанную информацию о значках гильдии.
    """
    sitedev:    bool = False
    verified:   bool = False
    partner:    bool = False
    favorite:   bool = False
    bughunter:  bool = False
    easteregg:  bool = False
    botdev:     bool = False
    youtube:    bool = False
    twitch:     bool = False
    spamhunt:   bool = False
    raw: SdcRawGuildStatus = SdcRawGuildStatus()


@dataclass
class SdcGuild:
    """
    Тип данных хранящий обработанную информацию о гильдии.

    Пример:
        SdcGuild.id: 1234567890
        SdcGuild.avatar: "https://cdn.discordapp.com/icons/{SdcGuild.id}/a_8f05534e4f750cf535988ae8a91fe9ad.gif",
        SdcGuild.lang: "ru"
        SdcGuild.name: "SD.Community"
        SdcGuild.description: "Описание сервера"
        SdcGuild.invite: "https://discord.gg/ABCDEF",
        SdcGuild.owner: "MegaVasiliy007#3301",
        SdcGuild.online: 250
        SdcGuild.members: 500
        SdcGuild.bot: 1
        SdcGuild.boost: 3
        SdcGuild.status: SdcGuildStatus
        SdcGuild.upCount: 299
        SdcGuild.tags: ["communication", "programming", "community"]
    """
    id:             int = 0
    online:         int = 0
    members:        int = 0
    bot:            int = 0
    boost:          int = 0
    upCount:        int = 0
    tags:           list = field(default_factory=list)
    avatar:         str = None
    lang:           str = "ru"
    name:           str = None
    description:    str = None
    invite:         str = None
    owner:          str = None
    status:         SdcGuildStatus = SdcGuildStatus()


@dataclass
class SdcGuildRates:
    """
    Тип данных хранящий обработанную информацию о голосах гильдии.

    Пример:

    SdcGuildRates.plus: [000000000000000000, 111111111111111111] # id пользователей
    SdcGuildRates.plus: [222222222222222222, 333333333333333333] # id пользователей
    SdcGuildRates.plus_count: 15                                 # количество пользователей поставивших "+"
    SdcGuildRates.minus_count: 15                                # количество пользователей поставивших "-"
    """
    plus:           list = field(default_factory=[])
    minus:          list = field(default_factory=[])
    plus_count:     int = 0
    minus_count:    int = 0


@dataclass
class SdcGuildPlace:
    """
    Тип данных хранящий обработанную информацию о месте гильдии в топе на сайте.

    Пример:

    SdcGuildPlace.place: 123
    """
    place: int = 0

