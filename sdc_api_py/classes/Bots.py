from typing import Union
from discord.ext.commands import Bot, AutoShardedBot


class Global:
    SDC_token = ""
    time = 60
    logging_level = None
    fork_name = ""


class Bots:

    def __init__(self, bot: Union[Bot, AutoShardedBot], token: str, fork_name:str = "discord", logging:bool = True):
        if not token.startswith("SDC "):
            token = "SDC " + token
        self.SDC_token = token
        self.bot = bot
        Global.SDC_token = self.SDC_token
        Global.logging_level = logging
        Global.fork_name = fork_name

    def create_loop(self, time:int = 60):
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