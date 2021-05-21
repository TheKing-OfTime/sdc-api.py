from dataclasses import dataclass, field


@dataclass
class SdcRawGuildStatus:
    """
    Тип данных хранящий исходную информацию о значках гильдии, прямиком с API.
    Так же тип хранит битовые згачения всех существующих значков
    """
    status:     int = 0
    sitedev:    hex = 0x1
    verified:   hex = 0x2
    partner:    hex = 0x4
    favorite:   hex = 0x8
    bughunter:  hex = 0x10
    easteregg:  hex = 0x20
    botdev:     hex = 0x40
    youtube:    hex = 0x80
    twitch:     hex = 0x100
    spamhunt:   hex = 0x200


@dataclass
class SdcRawGuild:
    """
    Тип данных хранящий исходную информацию о гильдии, прямиком с API.

    Пример:
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
        SdcRawGuild.status: 8
        SdcRawGuild.upCount: 299
        SdcRawGuild.tags: "communication,programming,community"
    """

    online:         int
    members:        int
    bot:            int
    boost:          int
    upCount:        int
    tags:           str
    owner:          str = None
    avatar:         str = None
    lang:           str = None
    name:           str = None
    description:    str = None
    invite:         str = None

    status: SdcRawGuildStatus = SdcRawGuildStatus


@dataclass
class SdcRawGuildRates:
    """
    Тип данных хранящий исходную информацию о голосах гильдии, прямиком с API.

    Пример:

    SdcRawGuildRates.rates:
    {
        "000000000000000000": 1,            # "id пользователя": состояние (0: голос против; 1: голос за)
        "111111111111111111": 1,
        "222222222222222222": 1,
        "333333333333333333": 1
    }
    """
    rates: dict


@dataclass
class SdcRawUserRates:
    """
    Тип данных хранящий исходную информацию о голосах пользователя, прямиком с API.

    Пример:
    SdcRawUserRates.rates:
    {
        "000000000000000000": 1,            # "id гильдии": состояние (0: голос против; 1: голос за)
        "111111111111111111": 1,
        "222222222222222222": 1,
        "333333333333333333": 1
    }
    """
    rates: dict


@dataclass
class SdcRawGuildPlace:
    """
    Тип данных хранящий исходную информацию о месте гильдии в топе на сайте, прямиком с API.

    Пример:

    SdcRawGuildPlace.place: 123
    """
    place: int


@dataclass
class SdcRawNikaWarns:
    """
    Тип данных хранящий исходную информацию о количестве варнов в системе Nika, прямиком с API.

    Пример:

    SdcRawGuildPlace.id: 000000000000000000
    SdcRawGuildPlace.type: "user"
    SdcRawGuildPlace.warns: 3
    """
    id:     int
    type:   str
    warns:  int
