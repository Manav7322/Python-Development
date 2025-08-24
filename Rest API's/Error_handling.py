import requests

try:
    res=requests.get("https://httpbin.org/delay/0",timeout=1)
    #headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    res.raise_for_status()
    print(res.json())
except requests.Timeout:
    print("Request timed out!")
except requests.RequestException as e:
    print("Error:", e)