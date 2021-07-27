from typing import Union
from discord.ext.commands import Bot, AutoShardedBot


class Global:
    SDC_token = ""
    time = 60
    logging_level = None


class Bots:

    def __init__(self, bot: Union[Bot, AutoShardedBot], token: str, logging:bool = True):
        if not token.startswith("SDC "):
            token = "SDC " + token
        self.SDC_token = token
        self.bot = bot
        Global.SDC_token = self.SDC_token
        Global.logging_level = logging

    def create_loop(self, time=60):
        time = int(time)

        if time < 30:
            time = 30

        Global.time = time
        try:
            self.bot.load_extension(".classes.extension", package="sdc_api_py")
        except Exception as e:
            print(e)
        else:
            print(f"SDC: Цикл успешно запущен. Статистика будет обновляться каждые {Global.time} минут")