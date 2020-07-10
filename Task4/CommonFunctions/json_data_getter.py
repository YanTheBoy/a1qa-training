import json


class JsonDataGetter:
    with open('../CommonFunctions/config.json', encoding='utf-8') as config_data:
        data = json.load(config_data)
    browser = data['browser']
    url = data['url']
    lang = data['language']


class AssertData:
    with open('../testsuites/asserts_data.json', encoding='utf-8') as a_data:
        asserts_data = json.load(a_data)
    research = asserts_data['research_page']
    trims = asserts_data['trims']
    comparison = asserts_data['comparison']
