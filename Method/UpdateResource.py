import json

import jsonpath
import requests

# APi Url
url = "https://reqres.in/api/users?page=2"

# read input json file
file = open("D:/api", 'r')
json_input = file.read()
requests_json = json.loads(json_input)


response = requests.put(url, requests_json)
print(response.status_code)


#validating response code
if response.status_code == 200:
    assert True
else:
    assert False


#parse res into jsonformat
response_json = json.loads(response.text)

#pick id using json path

print(jsonpath.jsonpath(response_json, 'updatedAt'))