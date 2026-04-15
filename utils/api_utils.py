import requests, json
from utils.file_utils import get_json_from_file


def get_api_data(url, op_header=None):
    header = {'Content_Type': 'application/json'}
    header = (header | op_header) if isinstance(op_header, dict) else header
    response = requests.get(url, verify=False, headers=header)
    print("\nRequest URL: ", url)
    print("request Header: ", response.request.headers)
    print("Response header: ", response.headers)
    return response


def post_api_data(url, body, op_header=None):
    header = {'Content_Type': 'application/json'}
    print("\nRequest URL: ", url)
    print("Request Body: ", json.dumps(body))
    request = requests.post(url, json=body, verify=False, headers=header)
    return request
