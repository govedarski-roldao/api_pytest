import requests, json


def get_api_data(url):
    header = {'content-type': 'application/json'}
    response = requests.get(url, verify=False, headers=header)
    return response
