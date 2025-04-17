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
from logging.handlers import RotatingFileHandler

from pyrogram import Client, filters
from pytgcalls import PyTgCalls

import config

StartTime = time.time()

# Fix Windows console encoding
if platform.system() == "Windows":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer)

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logging with UTF-8 encoding and rotating file handler
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs/FallenMusic.log",
            maxBytes=50000000,
            backupCount=10,
            encoding='utf-8'
        ),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

# Clear screen based on OS
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

# Create necessary directories
try:
    os.makedirs("downloads", exist_ok=True)
    os.makedirs("cache", exist_ok=True)
    LOGGER.info("Created necessary directories")
except Exception as e:
    LOGGER.error(f"Failed to create directories: {e}")
    sys.exit(1)

# Initialize Pyrogram clients
try:
    app = Client(
        "FallenMusic",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN,
        plugins=dict(root="FallenMusic/Plugins")
    )
    app2 = Client(
        "FallenAss",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        session_string=str(config.SESSION),
        plugins=dict(root="FallenMusic/Plugins")
    )
    LOGGER.info("Initialized Pyrogram clients")
except Exception as e:
    LOGGER.error(f"Failed to initialize Pyrogram clients: {e}")
    sys.exit(1)

# Initialize PyTgCalls
try:
    pytgcalls = PyTgCalls(app2)
    LOGGER.info("Initialized PyTgCalls")
except Exception as e:
    LOGGER.error(f"Failed to initialize PyTgCalls: {e}")
    sys.exit(1)

SUDOERS = filters.user()
SUNAME = config.SUPPORT_CHAT

async def fallen_startup():
    try:
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
            LOGGER.info("Joined support chats")
        except Exception as e:
            LOGGER.warning(f"Failed to join support chats: {e}")

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
        except Exception as e:
            LOGGER.error(f"Failed to send startup message: {e}")

        LOGGER.info("[•] Zefron Music Clients Booted Successfully.")
    except Exception as e:
        LOGGER.error(f"Error during startup: {e}")
        sys.exit(1)

try:
    asyncio.get_event_loop().run_until_complete(fallen_startup())
except KeyboardInterrupt:
    LOGGER.info("Bot stopped by user")
    sys.exit(0)
except Exception as e:
    LOGGER.error(f"Fatal error during startup: {e}")
    sys.exit(1)
