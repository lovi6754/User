import asyncio
import importlib
from pyrogram import Client, idle
from Zaid.helper import join
from Zaid import clients, app, ids
import Zaid
import aiohttp
from Zaid import clients, app, ids

async def start_bot():
    Zaid.aiosession = aiohttp.ClientSession()
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("Zaid.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
await Zaid.aiosession.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
