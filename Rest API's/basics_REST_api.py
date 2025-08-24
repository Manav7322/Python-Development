import requests

url="https://jsonplaceholder.typicode.com/todos/1"
# Every HTTP response comes with a status code:
# 200 = success
# 404 = Not Found

# 401 = Unauthorized (wrong/missing API key)

# 500 = Server error

response=requests.get(url)

if response.status_code==200:
    print("success:",response.json())
else:
    print("Error:",response.status_code)
print(response.status_code)
print(response.json())

# json parsing

# API's ususally send json(a dict in python)
data=response.json()

print(data["title"])

# Example with nested JSON:
res=requests.get(url)
user=res.json()

print(user["id"]) #simple key
# print(user["address"]["city"]) #nested json

# Query Parameters
# instead of fetching all the data we can use queries to fetch the specific data 
params={"userId":1}
res1=requests.get(url,params=params)
print(res1.url)