from dataclasses import dataclass, field


@dataclass
class SdcRawNikaWarns:
    """
    Тип данных хранящий обработанную информацию о количестве варнов в системе Nika.

    Пример:

    SdcGuildPlace.id: 000000000000000000
    SdcGuildPlace.type: "user"
    SdcGuildPlace.warns: 3
    """
    id:     int
    type:   str
    warns:  int
