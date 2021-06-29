import discord

from ..Bots import Global
from ..Lib import Querier
from discord.ext.tasks import loop
from discord.ext.commands import Cog


class Monitoring(Cog):
    def __init__(self, bot: discord.ext.commands.Bot):
        self.bot = bot
        self.querier = Querier()
        self.monitorings.start()
        self.last_server_count = -1

    @loop(minutes=Global._time)
    async def monitorings(self):
        server_count = len(self.bot.guilds)
        if server_count != self.last_server_count:
            try:
                res = await self.querier.execute_post_query(
                    f"https://api.server-discord.com/v2/bots/{self.bot.user.id}/stats",
                    headers={"Authorization": f"{Global.SDC_token}"},
                    data={"shards": self.bot.shard_count or 1, "servers": len(self.bot.guilds)}
                )
                self.last_server_count = server_count
                print(f"SDC Status updated: {await res.json()}")

            except Exception as error:
                print(error)
        else:
            print("SDC: Количество серверов не изменилось. Отправка статистики пропущена")


def setup(bot):
    bot.add_cog(Monitoring(bot))