import configparser
from pathlib import Path

cfg_file = "petqa.ini"
cgg_file_directory = "config"

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)