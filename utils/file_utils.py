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


# get data from CSV as lsit
def get_data_as_list(file_name):
    file_path = test_data_dir / file_name
    with open(file_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        lines = list(reader)
    return lines


print(get_data_as_list("register_api_data_with_status.csv"))


# returns list of tuples, within tuples it's "list of inputs" and a scalar value for output-status
def get_data_as_tuple(file_name):
    data_list = get_data_as_list(file_name)
    list_of_tuples = []

    for line in data_list:
        line_tuple = (line[:2], line[2])
        list_of_tuples.append(line_tuple)
    # lsit comprehension
    new_list_2 = [(x[:2], x[2]) for x in data_list]
    return new_list_2

print(get_data_as_tuple("register_api_data_with_status.csv"))

# we can create a dict with list of zipped keys and values

