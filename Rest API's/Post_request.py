import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "Learning POST", "body": "This is cool!", "userId": 10}

res = requests.post(url, json=data)

print("Status Code:", res.status_code)
print("Response JSON:", res.json())
