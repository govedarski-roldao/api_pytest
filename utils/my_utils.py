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


def put_data(url, body):
    headers = {"content-type": "application/json"}
    print("Request URL: ", url)
    print("Request body: ", json.dumps(body))
    response = requests.put(url, json=body, headers=headers, verify=False)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken

def deleteData(url, opHeader=None):
    headers = {"content-type": "application/json"}
    print("Request URL: ", url)
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    print("Request body: ", json.dumps(opHeader))
    response = requests.delete(url, headers=headers, verify=False)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken