from dataclasses import dataclass, field


@dataclass
class SdcNikaWarns:
    """
    Тип данных хранящий обработанную информацию о количестве варнов в системе Nika.

    Пример:

    SdcRawNikaWarns.id: 000000000000000000
    SdcRawNikaWarns.type: "user"
    SdcRawNikaWarns.warns: 3
    """
    id:     int = 0
    type:   str = ''
    warns:  int = 0
