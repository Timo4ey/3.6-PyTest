import time

from selenium.webdriver.common.by import By


def test_find_the_button(browser, request):
    lang_of_counrty = request.config.getoption('language')
    browser.get(f"https://selenium1py.pythonanywhere.com/{lang_of_counrty}/catalogue/coders-at-work_207/")
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form button[type="submit"]')
    if lang_of_counrty == 'fr':
        assert button.text == "Ajouter au panier", f"The current language is {lang_of_counrty}, " \
                                               f"and button name is {button.text}"
    else:
        print("В задание описан только вызов для французского языка")
