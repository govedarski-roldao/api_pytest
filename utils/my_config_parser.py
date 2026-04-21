import configparser
from pathlib import Path

cfg_file = "petsqa.ini"
cgg_file_directory = "config"
cfg_file_Flask_app = "qa.ini"

config = configparser.ConfigParser()
config_flask = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR / cgg_file_directory / cfg_file
CONFIG_FILE_Flask_app = BASE_DIR / cgg_file_directory / cfg_file_Flask_app

config.read(CONFIG_FILE)
config_flask.read(CONFIG_FILE_Flask_app)


def get_pet_url_api():
    return config["pet"]["url"]


def get_store_url_api():
    return config["store"]["url"]


def get_flask_app_base_url():
    base_url = "http://" + config_flask["flaskapp"]["url"] + ":" + config_flask["flaskapp"]["port"] + "/api/"
    return base_url

print(get_pet_url_api())
print(get_flask_app_base_url())
