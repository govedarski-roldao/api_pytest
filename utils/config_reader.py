import configparser
from pathlib import Path

cfg_file = "petsqa.ini"
cgg_file_directory = "config"

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR / cgg_file_directory / cfg_file

config.read(CONFIG_FILE)

def get_pet_url_api():
    return config["pet"]["url"]

def get_store_url_api():
    return config["store"]["url"]

print(get_pet_url_api())
print(get_store_url_api())