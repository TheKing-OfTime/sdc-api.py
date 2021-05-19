# sdc-api.py
* Враппер для https://api.server-discord.com/v2
* Документация к API: https://dosc.server-discord.com/

## Установка

### Чтобы установить враппер нужно:
1. Создать в корневой папке вашего проекта папку sdc_api.
2. Скопировать в неё содержимое этого репозитория.

# Внимание!
## Враппер полностью асинхронен. Любые вызовы функций следует проводить только в асинхронных функциях

## Использование

### Враппер включает в себя 3 основных класса:



#### Monitoring

```py
import sdc_api

monitoring = sdc_api.Monitoring(SDC_TOKEN)

...
sdc_guild = await monitoring.get_guild(id)  # Использовать в асинхронной функции

sdc_guild_place = await monitoring.fetch_guild_place(id)  # Использовать в асинхронной функции

sdc_guild_rate = await monitoring.get_guild_rate(id)  # Использовать в асинхронной функции

sdc_user_rate = await monitoring.get_user_rate(id)  # Использовать в асинхронной функции
```

#### NikaWarns

```py
import sdc_api

Nika = sdc_api.NikaWarns(SDC_TOKEN)

...
warns = await Nika.fetch_warns(id)  # Использовать в асинхронной функции
```

#### Bots

```py
import sdc_api
from discord.ext import commands

class BotsSDC(commands.Cog):

    def __init__(self, bot):
    self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        bots = sdc_api.Bots(self.bot, SDC_TOKEN)
        bots.create_loop()  #Как аргумент можно время в минутах. Раз в это количество минут будет отправляться статистика.

bot.add_cog(BotsSDC(bot))
```
