import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://google.com')
    return
    driver.quit()

@pytest.mark.usefixtures('init_driver')
def test_google_titlle(init_driver):
    assert driver.title == ""

@pytest.mark.usefixtures('init_driver')
def test_google_url(init_driver):
    assert driver.current_url == 'https://www.google.com/'
