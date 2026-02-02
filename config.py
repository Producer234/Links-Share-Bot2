import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "7753899951"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "link")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @PR_X_MAIN_CHANNEL</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC = "https://res.cloudinary.com/dqs0i4x9y/image/upload/v1756229930/rnlz6y6n5g4k7answrl9.jpg"
START_IMG = "https://res.cloudinary.com/dqs0i4x9y/image/upload/v1757045319/kxzmvhmjyxyi7ub0a90x.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/ALL_PR_BOTS'>ᴘʀ</a></blockquote></b>")

HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/owner_of_pr>ᴘʀ</a>\n» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href=https://t.me/PR_X_MAIN_CHANNEL>ᴘʀ ɴᴇᴛᴡᴏʀᴋ</a>\n» ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/PR_LINK_SHARE_BOT?start=req_LTEwMDIyODExMTAxMzc></a>\n» ᴄᴏᴍᴘʟᴇᴛᴇ ᴀɴɪᴍᴇ: <a href=https://t.me/all_ongoing_anime_in_hindi_dub>ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/owner_of_pr>ᴘʀ</a></b>")

ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>ᴛʜɪs ʙᴏᴛ ɪs ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ᴘʀ (@OWNER_OF_PR) ᴛᴏ sᴇᴄᴜʀᴇʟʏ sʜᴀʀᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ ʟɪɴᴋs ᴡɪᴛʜ ᴛᴇᴍᴘᴏʀᴀʀʏ ɪɴᴠɪᴛᴇ ʟɪɴᴋs, ᴘʀᴏᴛᴇᴄᴛɪɴɢ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɪɴᴛʏ: <a href='https://t.me/PR_X_MAIN_CHANNEL'>ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ᴘʀ</a>
<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/ALL_PR_BOTS'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/owner_of_pr'>ᴘʀ</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>ᴘʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>ᴍᴏɴɢᴏ ᴅʙ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @OWNER_OF_PR</b></blockquote>"""

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/PR_LINK_SHARE_BOT?start=req_LTEwMDIyODExMTAxMzc'>ᴀɴɪᴍᴇ ɪɴ ʜɪɴᴅɪ</a>
<blockquote expandable>›› ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs: <a href='https://t.me/+o5Iu2ApkDeFkNmU1'>ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs</a>
›› ᴘʀ ᴀʟʟ ʙᴏᴛ: <a href='https://t.me/ALL_PR_BOTS'>ᴘʀ ᴀʟʟ ʙᴏᴛ</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/MAIN_CHANNEL_H'>ʜᴀʀᴇᴍ ʀᴇᴀʟᴍ</a>
›› ᴀʙᴏᴜᴛ ᴘʀ: <a href='https://t.me/PR_LINK_SHARE_BOT?start=req_LTEwMDMyNDI0MTU5Nzk'>ᴀʙᴏᴜᴛ ᴘʀ</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/PR_X_MAIN_CHANNEL'>ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ᴘʀ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @OWNER_OF_PR</b></blockquote>""" 

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "8045158351").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(8045158351)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)