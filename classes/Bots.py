from discord.ext.commands import Bot


class Global:
    SDC_token = ""
    _time = 60


class Bots:

    def __init__(self, bot: Bot, token):
        self.SDC_token = token
        self.bot = bot
        Global.SDC_token = self.SDC_token

    def create_loop(self, time=60):
        time = int(time)

        if time < 30:
            time = 30

        Global._time = time
        try:
            self.bot.load_extension("extension.default_extension")
        except Exception as e:
            print(e)
        else:
            print(f"Цикл успешно запущен. Статистика будет обновляться каждые {Global._time} минут")