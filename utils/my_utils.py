import requests, json, random


# get API call and return response data
def get_api_data(url):
    headers = {"content-type": "application/json"}
    print("Request URL: ", url)
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    print(data)
    assert len(data) > 0, "empty response!!!!"
    return data, response.status_code, time_taken
