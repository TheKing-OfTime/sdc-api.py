import asyncio
import sdc_api_py

USER_ID = 348444859360608256

TOKEN = "" #SDC token. Можно получить на странице бота

Nika = sdc_api_py.NikaWarns(TOKEN)


async def test():

    warns = Nika.fetch_warns(USER_ID)

asyncio.run(test())