import asyncio
import sys
import logging

# --- CRITICAL FIX FOR PYTHON 3.12+ / 3.14 ---
# [span_4](start_span)This must happen BEFORE importing pyrogram to prevent "RuntimeError: No current event loop"[span_4](end_span)
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
# --------------------------------------------

from datetime import datetime
from pyrogram import Client
from pyrogram.enums import ParseMode
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, PORT, OWNER_ID
from plugins import web_server
import pyrogram.utils
from aiohttp import web

# Fix for specific channel IDs
pyrogram.utils.MIN_CHANNEL_ID = -1003515148046

name = """
Links Sharing Started
"""

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self, *args, **kwargs):
        # [span_5](start_span)[span_6](start_span)Validate critical config to avoid "Empty host" crashes[span_5](end_span)[span_6](end_span)
        if not TG_BOT_TOKEN:
            self.LOGGER(__name__).error("TG_BOT_TOKEN is missing!")
            return

        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Notify owner of bot restart
        try:
            await self.send_message(
                chat_id=OWNER_ID,
                text="<b><blockquote>🤖 Bot Restarted ♻️</blockquote></b>",
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
            self.LOGGER(__name__).warning(f"Failed to notify owner ({OWNER_ID}) of bot start: {e}")

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("Bot Running..!\n\nCreated by \nhttps://t.me/Pr_x_main_channel")
        self.LOGGER(__name__).info(f"{name}")
        self.username = usr_bot_me.username

        # Web-response server
        try:
            app = web.Application()
            # Ensure web_server() returns a valid setup
            router = await web_server()
            app.add_subapp("/webhook", router) if hasattr(router, 'add_subapp') else app.add_routes(router)
            
            runner = web.AppRunner(app)
            await runner.setup()
            bind_address = "0.0.0.0"
            # [span_7](start_span)PORT must be an integer[span_7](end_span)
            await web.TCPSite(runner, bind_address, int(PORT)).start()
            self.LOGGER(__name__).info(f"Web server started on {bind_address}:{PORT}")
        except Exception as e:
            self.LOGGER(__name__).error(f"Failed to start web server: {e}")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

# Global cancel flag for broadcast
is_canceled = False
cancel_lock = asyncio.Lock()

if __name__ == "__main__":
    # Use the established loop to run the bot
    Bot().run()
