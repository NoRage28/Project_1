import logging
from configparser import ConfigParser

logging.basicConfig(level='INFO')
logger = logging.getLogger()

file = 'config.ini'
config = ConfigParser()
config.read(file)
config_bot = config["bot"]
NUMBER_OF_USERS = int(config_bot['number_of_users'])
MAX_POSTS_PER_USER = int(config_bot['max_posts_per_user'])
MAX_LIKES_PER_USER = int(config_bot['max_likes_per_user'])
