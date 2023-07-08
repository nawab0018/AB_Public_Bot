# © Telegram @HMF_Owner_1, GitHub @ThiruXD 

import os
import time 


class Config(object):
	API_ID = int(os.environ.get("API_ID", "23532226"))
	API_HASH = os.environ.get("API_HASH", "f201fbe1399ebe8838f765cffb8d6ce5")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6328629995:AAFCG2R4P-eKRpowR2WgQp4XMAN1ACCAppg")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "AB_FileStore_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001812283852"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5140601098"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abmovieshouse1:abmovieshouse1@cluster0.gtacdwd.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001985963284")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001928760472")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "5657515019").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BASE_SITE = os.environ.get("BASE_SITE", "vnshortener.com")
	DOMAIN = os.environ.get("DOMAIN", "vnshortener.com")
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [AMIR BISTA](https://t.me/AB_BotZ_Update)

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

👑 **Owner:** @Ab_Admin0

🧑🏻‍💻 **Developer:** @Ab_Admin0

👥 **Support Group:** @abmovierequestgroup

📢 **Updates Channel:** @AB_BotZ_Update
"""
	ABOUT_DEV_TEXT = f"""
**🌐 This Bot Was Devloped By** : @Ab_Admin0"""
	SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, `/apikey api`
            
Ex: `/apikey 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
START_MEDIA = "https://graph.org/file/90be379764e989df8b35e.jpg"
START_TEXT = """Hɪ/Hᴇʟʟᴏ [{}](tg://user?id={})

I'ᴍ Uʟᴛʀᴀ Fᴀsᴛ Tᴇʟᴇɢʀᴀᴍ Cᴏᴜʟᴅ Sᴛᴏʀᴀɢᴇ Bᴏᴛ  Fᴏʀ  Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇs/Lɪɴᴋs Aɴᴅ Sᴇʟᴇᴄᴛ Mᴇᴛʜᴏᴅ Wᴀɪᴛ Fᴇᴡ Sᴇᴄᴏɴᴅs Bᴏᴛ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅ Tᴏ Oᴜʀ Sᴇʀᴠᴇʀ Aɴᴅ Gᴇɴᴀʀᴀᴛᴇ   ......

Cᴜʀʀᴇɴᴛʟʏ Sᴜᴘᴘᴏʀᴛᴇᴅ Fᴏʀᴍᴀᴛs :

• Lɪɴᴋs - Aʟsᴏ Sᴜᴘᴘᴏʀᴛ Bᴜʟᴋ Lɪɴᴋs 
• Fɪʟᴇs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Vɪᴅᴇᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Aᴜᴅɪᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Pʜᴏᴛᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB

Mᴏʀᴇ Fᴏʀᴍᴀᴛs Cᴏᴍᴍɪɴɢ Sᴏᴏɴ ......

Pᴏᴡᴇʀᴇᴅ Bʏ : [AMIR BISTA](http://t.me/Ab_Admin0)"""

HELP_TEXT = """Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Wᴇʙsɪᴛᴇ:

Sᴛᴇᴘ Nᴏ 1 : Jᴜsᴛ Cʟɪᴄᴋ 'Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ' Bᴜᴛᴛᴏɴ Aɴᴅ Cᴏᴘʏ Yᴏᴜʀ  Aᴄᴄᴏᴜɴᴛ Aᴘɪ Tᴏᴋᴇɴ.

Sᴛᴇᴘ Nᴏ 2 : Tʜᴇɴ Cᴏᴍ Aɢᴀɪɴ Hᴇʀᴇ Aɴᴅ Usᴇ /api Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Yᴏᴜʀ [SHORTENER] Aᴄᴄᴏᴜɴᴛ.

Exᴀᴍᴘʟᴇ : `/api s18ғsjsn737d19f08f382h19d9sd473774hd58` """

ABOUT_TEXT = """🤖 Name :  AB FILE STORE BOT 

🔠 Language  : Python3
📚 Library   : Teleton And Pyrogram
👑 Owner     : @Ab_Admin0
🧑🏻‍💻 Developer : @Ab_Admin0

©️Powered By @abmoviehouse """



