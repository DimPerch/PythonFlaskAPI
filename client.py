import requests
import json


URL = 'http://localhost:5000/api/v1.0/users'

r = requests.post(URL, data={"first_name": "dimitry", "last_name": "perchatkin"})
answer = json.loads(r.text)
new_id = answer.get('result').get('User').get('id')
print(answer)

r = requests.get(URL, data={"id": new_id})
print(r.text)

r = requests.put(URL, data={"id": 55, "first_name": "Dimitry", "last_name": "Perchatkin"})
print(r.text)

r = requests.get(URL, data={"id": new_id})
print(r.text)
