import asyncio
import sdc_api_py

USER_ID = 348444859360608256

GUILD_ID = 669961614434500620

TOKEN = "" #SDC token. Можно получить на странице бота

Monitoring = sdc_api_py.Monitoring(TOKEN)


async def test():
    guild = await Monitoring.get_guild(GUILD_ID)

    guild_place = await Monitoring.fetch_guild_place(GUILD_ID)

    guild_rete = await Monitoring.get_guild_rate(GUILD_ID)

    user_rete = await Monitoring.get_user_rate(USER_ID)

asyncio.run(test())
