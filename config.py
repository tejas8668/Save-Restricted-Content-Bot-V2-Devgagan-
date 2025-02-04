# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6018060368").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://tejaschavan1110:jkZSAYN4iWHRq1CM@cluster0.trwix.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002465239145")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002465239145"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "3600"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "3600"))
WEBSITE_URL = getenv("WEBSITE_URL", "gplinks.com")
AD_API = getenv("AD_API", "89e6e36b347f3db3f187dda37290c5927e99c18a")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
