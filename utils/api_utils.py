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


def delete_api_data(url, user_id, token, op_header=None):
    header = {
        'Content-Type': 'application/json',
        "x-access-token": token
    }

    if isinstance(op_header, dict):
        header.update(op_header)

    print("\nRequest URL: ", url)
    print("Request Body: ", json.dumps({"id": user_id}))
    print("Request Header: ", header)

    response = requests.delete(
        url,
        json={"id": user_id},
        verify=False,
        headers=header
    )

    return response


def new_del_api(url, body, op_header=None):
    headers = {"content-type": "application/json"}
    headers = (headers | op_header) if isinstance(op_header, dict) else headers
    response = requests.delete(url, json=body, headers=headers, verify=False)
    return response