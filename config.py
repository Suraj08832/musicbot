import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Basic Config
API_ID = int(getenv("API_ID", "28053244"))
API_HASH = getenv("API_HASH", "a7d745be7c8ba465750bfad1e7abc075")
BOT_TOKEN = getenv("BOT_TOKEN", "7547565072:AAEShATtAbQVAx6_AkbSLP69l9Kn3FlNXtA")
OWNER_ID = int(getenv("OWNER_ID", "1356469075"))
SESSION = getenv("SESSION", "BQGsDvwAh_iDhIIhT5kD5VTi4Y3uR7f2hwoQ3Dl0vd7d9REqD0OuE-AqUijF-Ntnt715Qmmak9EdLcTGHqE6d4uUOqDjqgakzCns_AGnO79yptFMHeyvlGnFHmxIfyLrvj7zkM0cyKK4V1CJSoRqhlrFovA9mO8N0vRzuqwRK62hoZCniD6vZ72ymI_VhbjQG9j9K2J3R4q6t3Xr7kD98S-GVGbvYa8dwa_JgN6nqOu4OY896jO3faX0gAVUwjoFnuMFRGMwDBe_g5PRxcTh8cv7NM2vCf6T_HjTExtfHAw9x3FccIMAmI9D9-XwqZzmSbynZiLq-BEN2-I8SOQVWzk1xXbUggAAAAHmg7_MAA")

# String Session
STRING = getenv("STRING", SESSION)

# Optional Config
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "zefronmusic")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "ZEFRONAssociation")

# Do Not Change
COMMAND_PREFIXES = ["/", "!", "."]
BANNED_USERS = set()
OWNER_ID = int(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

# Assistant Config
ASS_ID = 8162361292
ASS_NAME = "testing"
ASS_USERNAME = "testing3353"
ASS_MENTION = f"[{ASS_NAME}](https://t.me/{ASS_USERNAME})"
