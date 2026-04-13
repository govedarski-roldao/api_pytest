import requests, json


def get_api_data(url,op_header=None):
    header = {'Content_Type': 'application/json'}
    header = (header | op_header) if isinstance(op_header, dict) else header
    response = requests.get(url, verify=False, headers=header)
    print("\nRequest URL: ", url)
    print("request Header: ", response.request.headers)
    print("Response header: ", response.headers)
    return response
