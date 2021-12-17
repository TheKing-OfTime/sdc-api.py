import importlib

from ..Bots import Global
from ..Lib import Querier

discord = importlib.import_module(f'{Global.fork_name}')
tasks = importlib.import_module(f'{Global.fork_name}.ext.tasks')
commands = importlib.import_module(f'{Global.fork_name}.ext.commands')

class Monitoring(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.querier = Querier()
        self.monitorings.start()
        self.last_server_count = -1

    @tasks.loop(minutes=Global.time)
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
                if res.content_type == 'application/json':
                    data = await res.json()
                else:
                    raise RuntimeError
                status = data["status"]
                if status is True:
                    if Global.logging_level:
                        print(f"SDC: Статистика отправлена")
                else:
                    print(f"SDC: Произошла ошибка при отправке статистики: {data}")

            except RuntimeError:
                print(f"SDC: Произошла ошибка при отправке статистики: API временно недоступно. Повторное подключение через {Global.time}")
            except Exception as err:
                print(f"SDC: Произошла неизвестаня ошибка при отправке статистики: {err}")
        else:
            if Global.logging_level:
                print("SDC: Количество серверов не изменилось. Отправка статистики пропущена")


def setup(bot):
    bot.add_cog(Monitoring(bot))