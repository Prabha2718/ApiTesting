import jsonpath
import requests
import json

# APi Response
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

# Display response content
response.content
# print(request)

# parse response to json format
json_res = json.loads(response.text)
print(json_res)

# Fetch the json path
first_name = jsonpath.jsonpath(json_res, 'total')
assert first_name[0] == 1
