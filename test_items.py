import time

from selenium.webdriver.common.by import By


def test_find_the_button(browser, request):
    lang_of_counrty = request.config.getoption('language')
    browser.get(f"https://selenium1py.pythonanywhere.com/{lang_of_counrty}/catalogue/coders-at-work_207/")
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, '#add_to_basket_form button[type="submit"]')
    assert len(button) > 0, "Button not found"
