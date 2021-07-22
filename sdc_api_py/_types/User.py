from dataclasses import dataclass, field


@dataclass
class SdcUserRates:
    """
    Тип данных хранящий обработанную информацию о голосах пользователя.

    Пример:

    SdcUserRates.plus: [000000000000000000, 111111111111111111] # id гильдий
    SdcUserRates.plus: [222222222222222222, 333333333333333333] # id гильдий
    SdcUserRates.plus_count: 15                                 # количество гильдий которым пользователь поставил "+"
    SdcUserRatess.minus_count: 15                                # количество гильдий которым пользователь поставил "-"
    """

    plus:           list = field(default_factory=[])
    minus:          list = field(default_factory=[])
    plus_count:     int = 0
    minus_count:    int = 0
