import requests, json

# response = requests.get("https://www.google.com/search?q=pytest", verify=False)
#
# print(response.text)
# print(
#     "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# url = "https://regres.in/api/users"
# response_two = requests.get(url, verify=False)
# print(response_two.status_code)
# print(response_two.headers)
# print(response_two.request.headers)
# # print(response_two.json())
# print(response_two.headers["Content-Type"])
#
# print(
#     "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# url = "https://httpbin.org/get"
# my_params = {"key1": "value1", "key2": "value2"}
# r = requests.get(url, params=my_params)
# print(r.url)
#
# for key, value in r.json().items():
#     print(key, ": ", value)
# print(
#     "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
url = "https://httpbin.org/post"
paylaod = {"key1": "value1", "key2": "value2"}
headers = {"accept": "application/json", "content-type": "application/json"}
r = requests.post(url, json=paylaod, headers=headers, verify=False)
print(r.url)
print("status code: ", r.status_code)
print(r.text)
print(r.request.headers)
print(r.headers)
