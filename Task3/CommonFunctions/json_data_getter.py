import json


class JsonDataGetter:
    with open('../CommonFunctions/config.json') as config_data:
        data = json.load(config_data)
    browser = data['browser']
    url = data['url']
    lang = data['language']


class TestingData:
    with open('../testsuites/asserts_data.json') as a_data:
        asserts_data = json.load(a_data)
    year = asserts_data['age_year']
    client = asserts_data['steam_client_name']
    gamapege = asserts_data['gamepage_url']
    action_ru = asserts_data['action_game_ru']
    action_en = asserts_data['action_game_en']
    action_heading = [asserts_data['action_heading_ru'], asserts_data['action_heading_en']]
    indie_ru = asserts_data['indie_game_ru']
    indie_en = asserts_data['indie_game_en']
    indie_heading = [asserts_data['indie_heading_ru'], asserts_data['indie_heading_en']]


class KeyWordByLanguage:
    if JsonDataGetter.lang == 'ru':
        keywords = {
            'action': TestingData.action_ru,
            'indie': TestingData.indie_ru}
    elif JsonDataGetter.lang == 'en':
        keywords = {
            'action': TestingData.action_en,
            'indie': TestingData.indie_en}
