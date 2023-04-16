from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

driver = None

@pytest.fixture()
def test_yandex():
    driver = webdriver.Chrome()
    driver.get('https://yandex.com/')
    driver.implicitly_wait(5)


def search_input(test_yandex):
    search_box = test_yandex.find_element(By.CLASS_NAME, 'input__ahead')
    search_box.send_keys('Selenium pytest')
    search_box.send_keys(Keys.ENTER)
    # Verify the search results
    assert 'pytest' in test_yandex.title
