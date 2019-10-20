import time
from selenium.webdriver.common.by import By

def test_add_cart_button(browser):
 browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
 time.sleep(30)
 count = len(browser.find_elements(By.XPATH, "//form[@id='add_to_basket_form']//button[@type='submit']"))
 assert count == 1, 'Element not found'
    