## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "BABiMZkAk82dAm2xcffNjBF9lf7SrebT6XW97UzHWRqmx8x3uu_c5msyLHqcBD7aTZrJ7GLTr_MSvsyEON8gCeabUbLNZyNp8Q0uBW69tcubwiOryLNRdCXnwR2AVew9yymZf6PdlOTpZm-zCTF6YsfVTzWuSuhTRLCUbBeywZfK2vmDhgVYQsByMxJ_AsDH6fQd5oM7X1P150hdIRyZ2j0MCuwHqDoFnxBgZqYb0Jej0lBprqMth3TIsFquYhHcVh2IyTaxWMA5f7OIX5l8y6Qo_Er1tyVFNIhtCes1WLOnF9sAKpTDKneyBVKro4kBUimq2EoBalJnro_q6JcJZWlPkrsZSAAAAAFOcPpqAA":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6141992820:AAH0OEOZMzV7MU47ZdvlW-VNHtGkpslGg4s")
BOT_NAME = getenv("BOT_NAME", "ɢʀᴏᴜᴘ ᴍᴜsɪᴄ")

API_ID = int(getenv("API_ID", "20950629"))
API_HASH = getenv("API_HASH", "9139bc314a2dd1522043a363e61b07e4")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "فــــــانز𝐀𝐳𝐮𝐫𝐞•⏤‌❰𝐋𝐈𝐊𝐄 بّـــــــًسًـــــا۾❱ᴬʳᵃᵇˢ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Bssam_for5")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐁𝐒𝐒𝐀𝐌")
BOT_USERNAME = getenv("BOT_USERNAME", "musicxzreaswe_bot")
OWNER_ID = getenv("OWNER_ID", "6088000501")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "moreswa")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "papokm")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "cvxzasoe")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6294217355").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
