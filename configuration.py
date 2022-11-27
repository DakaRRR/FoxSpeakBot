import logging
from decouple import config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    TG_BOT_TOKEN = config('TG_BOT_TOKEN')
    TG_CHANNEL_ID = config('TG_CHANNEL_ID')
    logger.info("Env variables loaded")
    logger.info(f"Work with channel_id {TG_CHANNEL_ID}")
except (KeyError, ValueError):
    logger.critical(
        "Please, set correct env variables: \n"
        "  * TG_BOT_TOKEN\n  * TG_CHANNEL_ID")
    raise