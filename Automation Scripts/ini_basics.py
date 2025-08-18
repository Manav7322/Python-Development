import configparser

config = configparser.ConfigParser()
config.read("ini_basics.ini")
print(config.sections())
print(config["general"]["sort_by"])
print(config["extensions"]["images"])