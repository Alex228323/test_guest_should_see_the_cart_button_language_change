import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException   
import time

def test_guest_should_see_the_cart_button_language_change(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    def check_exists_by_xpath(xpath):
        try:
            browser.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True
    assert check_exists_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]') == True, "Элемент отсутствует"
    time.sleep(10)
