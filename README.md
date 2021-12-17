# sdc-api.py
* Враппер на Python для [SDC API](https://docs.server-discord.com)
* Документация к API: https://docs.server-discord.com/
* [Сервер поддержки](https://discord.gg/8epHXKA) враппера 

## Установка

```
pip install sdc_api_py
```

# Внимание!
## Враппер полностью асинхронен. Любые вызовы функций следует проводить только в асинхронных функциях

## Использование

### Враппер включает в себя 3 основных класса:



#### Monitoring

```py
import sdc_api_py

monitoring = sdc_api_py.Monitoring(SDC_TOKEN)

...
sdc_guild = await monitoring.get_guild(id)  # Использовать в асинхронной функции

sdc_guild_place = await monitoring.fetch_guild_place(id)  # Использовать в асинхронной функции

sdc_guild_rate = await monitoring.get_guild_rate(id)  # Использовать в асинхронной функции

sdc_user_rate = await monitoring.get_user_rate(id)  # Использовать в асинхронной функции
```

#### NikaWarns

```py
import sdc_api_py

Nika = sdc_api_py.NikaWarns(SDC_TOKEN)

...
warns = await Nika.fetch_warns(id)  # Использовать в асинхронной функции
```

#### Bots

```py
import sdc_api_py
from discord.ext import commands

class BotsSDC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):                       #Аргумент fork_name опциональный. Укажите название используемого форка discord.py если таковой используется.
                                                    #Название нужно указыать то, с помощью которого вы импортировали форк в свой проект.
        bots = sdc_api_py.Bots(self.bot, SDC_TOKEN, fork_name, logging) # Аргумент logging опциональный. По умолчанию True.
        bots.create_loop()  #Как аргумент можно использовать время в минутах. Раз в это количество минут будет отправляться статистика.
                            #По умолчанию 60 минут. Минимальный порог 30 минут.
bot.add_cog(BotsSDC(bot))
```
