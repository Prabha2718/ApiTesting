import json

import jsonpath
import requests

# APi Url
url = "https://reqres.in/api/users"

# read input json file
file = open("D:/api", 'r')
jsoninput = file.read()

requests_json = json.loads(jsoninput)
print(requests_json)

response = requests.put(url, requests_json)
print(response)

#validating response code
if response.status_code == 201:
    assert True
else:
    assert False

#fetch header from response
print(response.headers.get('Content-Type'))

#parse res into jsonformat
response_json = json.loads(response.text)

#pick id using json path

print(jsonpath.jsonpath(response_json, 'id'))