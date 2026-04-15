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


