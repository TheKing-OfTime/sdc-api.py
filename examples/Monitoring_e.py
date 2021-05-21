import asyncio
import sdc_api_py

SDC_TOKEN = "PLACE YOUR TOKEN HERE"
GUILD_ID = 500020124515041283
USER_ID = 329688477073539072

monitoring = sdc_api_py.Monitoring(SDC_TOKEN)


async def test():
    sdc_guild = await monitoring.get_guild(GUILD_ID)
    print(f"Name of guild: {sdc_guild.name}; Members amount: {sdc_guild.members}")

    sdc_guild_place = await monitoring.get_guild_place(GUILD_ID)
    print(f"Place of guild in server list: {sdc_guild_place.place}")

    sdc_guild_rate = await monitoring.get_guild_rate(GUILD_ID)
    print(f"Rating of guild on monitoring: {sdc_guild_rate.plus - sdc_guild_rate.minus}")

    sdc_user_rate = await monitoring.get_user_rate(GUILD_ID)
    print(f"Positive rates of user: {sdc_user_rate.plus_count}")

asyncio.run(test())
