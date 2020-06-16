import json


class JsonDataGetter:
    with open('../CommonFunctions/config.json') as config_data:
        data = json.load(config_data)
    browser = data['browser']
    url = data['url']
    lang = data['language']


class KeyWordByLanguage:
    if JsonDataGetter.lang == 'ru':
        keywords = {
            'action': 'Экшен',
            'indie': 'Инди'}
    elif JsonDataGetter.lang == 'en':
        keywords = {
            'action': 'Action',
            'indie': 'Indie'}

