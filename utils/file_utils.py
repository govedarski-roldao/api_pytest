import csv
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
test_data_dir = BASE_DIR / "TestData"
print(test_data_dir)


def get_json_from_file(file_name):
    file_path = test_data_dir / file_name
    with open(file_path, "r") as json_file:
        return json.load(json_file)


# function to read data from csv file
def get_csv_from_file(file_name):
    file_path = test_data_dir / file_name
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        dict_list = list(csv_reader)
        print(dict_list)
    return dict_list


getcsv = get_csv_from_file("register_api_data.csv")
