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

URL = 'http://localhost:5000/api/v1.0/articles'
r = requests.post(URL, data={"title": "PythonSuper", "text": "dimitry good chelovek",
                             "author_id": "9",
                             })
answer = json.loads(r.text)
new_id = answer.get('result').get('Article').get('id')
print(answer)

r = requests.get(URL, data={"id": new_id})
print(r.text)

r = requests.put(URL, data={"id": new_id, "title": "PythonPlox", "text": "dimitry bad chelovek",
                             "author_id": 67})
print(r.text)

r = requests.get(URL, data={"id": new_id})
print(r.text)

URL = 'http://localhost:5000/api/v1.0/comments'

r = requests.post(URL, data={"article_id": 1, "author_id": 2,
                             "text": "Good comment"})
answer = json.loads(r.text)
new_id = answer.get('result').get('Comment').get('id')
print(answer)

r = requests.get(URL, data={"id": new_id})
print(r.text)

r = requests.delete(URL, data={"id": new_id})
print(r.text)

r = requests.get(URL, data={"id": new_id})
print(r.text)

r = requests.put(URL, data={"id": 55, "article_id": 1, "author_id": 2,
                             "text": "Good comment"})
print(r.text)

r = requests.get(URL, data={"id": new_id})
print(r.text)
