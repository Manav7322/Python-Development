import requests

url="https://api.github.com/user/repos"

headers={"Authorization": "Bearer ghp_Your_github_token"}

res=requests.get(url,headers=headers)
for repo in res.json():
    print(repo["name"])

# content-type header 
url1="https://jsonplaceholder.typicode.com/posts"

header1={"Content-Type": "application/json"}

data={"title":"foo","body":"bar","userId":1}
res2=requests.post(url1,json=data,headers=header1)
print(res2.json())

# custom headers 

headers={
    "X-RapidAPI-Key" : "your_api_key",
    "X-RapidAPI-Host" : "exampleapi.p.rapidapi.com"
}