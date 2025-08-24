import requests

url="https://jsonplaceholder.typicode.com/posts/1"

data = {"id": 1, "title": "New Title", "body": "Completely new content", "userId": 1}
res=requests.put(url,json=data)
print("Statuc_Code:", res.status_code)
print("Response Json:", res.json())

data1={"title":"Patched title"}
res1=requests.patch(url, json=data1)
print(res1.status_code)
print(res1.json())

res2=requests.delete(url)
print(res2.status_code)
print(res2.json())
print(res.json())