import requests
import json  # for pretty printing

url = "https://jsonplaceholder.typicode.com/users"

res = requests.get(url)
data = res.json()

# Normal print (hard to read)
print("Raw JSON:\n", data)

# Pretty print
print("\nPretty JSON:\n")
print(json.dumps(data, indent=4))  # indent=4 gives nice formatting
