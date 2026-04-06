import json

dataDict = {
    "sampleString": "Great automation Framework",
    "sampleList": ["Good", "Better", "Best"],
    "sampleTuple": ("Python", "Pytest", "Automation"),
    "sampleObj": {"platform": "Udemy", "Valuable": True},
    "sampleInteger": 555,
    "booleanValue": True,
    "noneValue": None,
}

print("Convert pydict to Json")
resultJson = json.dumps(dataDict, indent=4)
print(resultJson)
print(type(resultJson))

data_dict = json.loads(resultJson)
print(type(data_dict))

with open("example.json", "r") as file:
    data = json.load(file)
    print(type(data))
    print(data)


def validate_json(data):
    try:
        json.loads(data)
    except ValueError as err:
        return False
    return True


JsonString = """{"name": "Raju", "salary": 3000, "email":"email@akhn.com"}"""
is_valid = validate_json(JsonString)
print("Json String passed is valid? ", is_valid)
