import discord

from ..Bots import Global
from ..Lib import Querier
from discord.ext.tasks import loop
from discord.ext.commands import Cog


class Monitoring(Cog):
    def __init__(self, bot: discord.ext.commands.Bot):
        self.bot = bot
        self.querier = Querier()

    @loop(minutes=Global._time)
    async def monitorings(self):
        try:
            res = await self.querier.execute_post_query(
                f"https://api.server-discord.com/v2/bots/{self.bot.user.id}/stats",
                headers={"Authorization": f"SDC {Global.SDC_token}"},
                data={"shards": self.bot.shard_count or 1, "servers": len(self.bot.guilds)}
            )

            await self.bot.get_channel(810967184397434921).send(f"SDC Status updated: {await res.json()}")
        except Exception as error:
            print(error)

def setup(bot):
    bot.add_cog(Monitoring(bot))