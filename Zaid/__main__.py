import asyncio
import importlib
import aiohttp

from pyrogram import idle
from Zaid.helper import join
from Zaid import clients, app, ids
from Zaid.modules import ALL_MODULES
import Zaid


async def start_bot():
    # Create aiohttp session
    Zaid.aiosession = aiohttp.ClientSession()

    # Start Bot Client
    await app.start()
    print("LOG: Founded Bot token Booting..")

    # Load Modules
    for module in ALL_MODULES:
        importlib.import_module(f"Zaid.modules.{module}")
        print(f"Successfully Imported {module} 💥")

    # Start User Clients
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(e)

    print("All Clients Started Successfully ✅")

    try:
        await idle()
    finally:
        await app.stop()

        for cli in clients:
            try:
                await cli.stop()
            except Exception:
                pass

        if Zaid.aiosession:
            await Zaid.aiosession.close()


if __name__ == "__main__":
    asyncio.run(start_bot())
