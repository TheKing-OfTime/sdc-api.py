from dataclasses import dataclass, field


@dataclass
class SdcUserRates:
    """
    Тип данных хранящий обработанную информацию о голосах пользователя.

    Пример:

    SdcGuildRates.plus: [000000000000000000, 111111111111111111] # id гильдий
    SdcGuildRates.plus: [222222222222222222, 333333333333333333] # id гильдий
    SdcGuildRates.plus_count: 15                                 # количество гильдий которым пользователь поставил "+"
    SdcGuildRates.minus_count: 15                                # количество гильдий которым пользователь поставил "-"
    """

    plus:           list
    minus:          list
    plus_count:     int = field(init=False)
    minus_count:    int = field(init=False)

    def __post_init__(self):
        self.plus_count = len(self.plus)
        self.minus_count = len(self.minus)
