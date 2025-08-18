import json

config = {
    "sort_by" : "date",
    "extensions" : {"images" : [".jpg",".png"]}
}

with open("config.json","w") as f:
    json.dump(config, f, indent=4)

with open("config.json","r") as f:
    config=json.load(f)

print(config["sort_by"])
print(config["extensions"]["images"])