import time

from selenium.webdriver.common.by import By



def test_find_the_button(browser, request):
    browser.get(f"https://selenium1py.pythonanywhere.com/{request.config.getoption('language')}/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button")
    time.sleep(1)
