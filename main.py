import asyncio
from bot import Bot

async def start_bot():
    # Use 'async with' to properly handle startup and shutdown
    async with Bot() as app:
        print("Bot started successfully!")
        # This keeps the bot running until you stop it
        await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
