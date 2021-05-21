from dataclasses import dataclass, field
from .Raw import SdcRawGuildStatus


@dataclass
class SdcGuildStatus:
    """
    Тип данных хранящий обработанную информацию о значках гильдии.
    """
    sitedev:    bool
    verified:   bool
    partner:    bool
    favorite:   bool
    bughunter:  bool
    easteregg:  bool
    botdev:     bool
    youtube:    bool
    twitch:     bool
    spamhunt:   bool
    raw: SdcRawGuildStatus = SdcRawGuildStatus


@dataclass
class SdcGuild:
    """
    Тип данных хранящий обработанную информацию о гильдии.

    Пример:
        SdcRawGuild.id: 0
        SdcRawGuild.avatar: "a_8f05534e4f750cf535988ae8a91fe9ad",
        SdcRawGuild.lang: "ru"
        SdcRawGuild.name: "SD.Community"
        SdcRawGuild.description: "Описание сервера"
        SdcRawGuild.invite: "https://discord.gg/ABCDEF",
        SdcRawGuild.owner: "MegaVasiliy007#3301",
        SdcRawGuild.online: 250
        SdcRawGuild.members: 500
        SdcRawGuild.bot: 1
        SdcRawGuild.boost: 3
        SdcRawGuild.status: SdcGuildStatus
        SdcRawGuild.upCount: 299
        SdcRawGuild.tags: ["communication", "programming", "community"]
    """
    id:             int
    online:         int
    members:        int
    bot:            int
    boost:          int
    upCount:        int
    tags:           list = field(default=list)
    avatar:         str = None
    lang:           str = "ru"
    name:           str = None
    description:    str = None
    invite:         str = None
    owner:          str = None
    status:         SdcGuildStatus = SdcGuildStatus


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
    plus:           list
    minus:          list
    plus_count:     int
    minus_count:    int


@dataclass
class SdcGuildPlace:
    """
    Тип данных хранящий обработанную информацию о месте гильдии в топе на сайте.

    Пример:

    SdcGuildPlace.place: 123
    """
    place: int

