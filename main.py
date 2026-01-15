import asyncio
import logging

# 1. Initialize the event loop BEFORE any other imports
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# 2. Now it is safe to import your bot
from bot import Bot

if __name__ == "__main__":
    try:
        # 3. Start the bot
        Bot().run()
    except Exception as e:
        logging.error(f"Bot failed to start: {e}")
