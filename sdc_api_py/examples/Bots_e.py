import sdc_api_py
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

TOKEN = "" #SDC token. Можно получить на странице бота

class BotsSDC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        bots = sdc_api_py.Bots(self.bot, TOKEN)
        bots.create_loop()  #Как аргумент можно использовать время в минутах. Раз в это количество минут будет отправляться статистика. По умолчанию 60 минут

bot.add_cog(BotsSDC(bot))