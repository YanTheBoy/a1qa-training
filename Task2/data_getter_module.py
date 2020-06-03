import json


class JsonDataGetter:
    with open('config.json') as config_data:
        data = json.load(config_data)
    browser = data['browser']
    url = data['url']
    path = data['path']
    with open('yandex-account.json') as user_info:
        info = json.load(user_info)
    login = info['login']
    password = info['password']
