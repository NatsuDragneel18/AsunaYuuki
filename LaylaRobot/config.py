# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
#import json
import os


# def get_user_list(config, key):
#    with open("{}/LaylaRobot/{}".format(os.getcwd(), config), "r") as json_file:
#        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 5699301  # integer value, dont use ""
    API_HASH = "5efb0cd88effcd5d1abc98b10bccc12f"
    TOKEN = "1886602051:AAFnCrpUPpvBCKggPEzpMpb077xy197ZvIM"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1249591948  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Yoga_CIC" 
    SUPPORT_CHAT = "YuukiAsunaSupportChat"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001517345448
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001368313136
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "mongodb+srv://asuna:asuna123@cluster0.9zv2k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    MONGO_DB_URI = "mongodb+srv://asuna:asuna123@cluster0.9zv2k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"  # needed for any database modules
    REDIS_URL = ""
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "0WZ1Dpb0_qjDjq0Z4NqAdF7H1RGLI1HhUVtHQ47VU6siLCeTePPIIVMDi6amvx_P"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
 #   DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
 #   DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
 #   DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
 #   TIGERS = get_user_list("elevated_users.json", "tigers")
 #   WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = "https://paypal.me/YogaPranataDMK"  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "MB415I6HA0VMCO8Y"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "9ZXF898UZC4J"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        " "  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = " "  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    OPENWEATHERMAP_ID = "53713b3c406eac9bfca775ce9a2001f2"
    BOT_ID = ""
    HEROKU_API_KEY = "014ce2a3-065e-4b88-a883-691087e2a7dc"
    HEROKU_APP_NAME = "asunabotx"
    VIRUS_API_KEY = " "
    TEMP_DOWNLOAD_DIRECTORY = "./downloads"
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
