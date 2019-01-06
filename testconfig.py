import configparser
config = configparser.ConfigParser()
config.read("./config/account.ini", encoding="utf8")
# print(config.options("account_user"))
user = config.get("account_user", "username")
print(user)
