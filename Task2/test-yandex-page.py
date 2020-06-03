import csv
import random
from data_getter_module import JsonDataGetter
from patterns.YandexMarketPages import SearchHelper


login = JsonDataGetter.login
password = JsonDataGetter.password
path = JsonDataGetter.path


def test_market_page_open(browser):
    market_page = SearchHelper(browser)
    market_page.wait(5)
    market_page.go_to_site()
    assert market_page.check_site_open() == 'Яндекс.Маркет', 'Yandex.market page is not opened.'

    top_categories = market_page.get_top_categories()
    market_page.click_enter_button()
    market_page.change_window_to_page('authorization')

    market_page.enter_login(login)
    market_page.click_login_button()
    market_page.enter_password(password)
    market_page.click_login_button()
    market_page.change_window_to_page('main')
    assert market_page.check_user_login() != 0, 'User is not logged in.'

    top_categories = top_categories
    selected_category = random.choice(top_categories)
    market_page.hide_popup_search_field()
    market_page.go_to_selected_category(selected_category)
    assert selected_category[:3].lower() in market_page.get_h1_text().lower(), 'Wrong category opened.'

    market_page.go_to_main_page()
    market_page.open_categories_tray()
    all_categories = [category.text for category in market_page.get_all_categories()]
    with open(path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        textwriter = csv.writer(csvfile)
        for category in all_categories:
            textwriter.writerow([category])
    assert check_list_similarity(top_categories, all_categories), 'Not all visible categories in total list.'

    market_page.click_on_user_icon(login)
    market_page.click_exit()
    assert market_page.find_enter_button(), 'User is still logged in.'


def check_list_similarity(temple_list, list_in):
    checklist = [category_name for category_name in temple_list
                 for category in list_in
                 if category_name[:4].lower() in category.lower()
                 ]
    return checklist == temple_list
