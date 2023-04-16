from selenium import webdriver
import pytest

driver = None

@pytest.fixture(scope='module')
def test_facebook():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    driver.implicitly_wait(10)
    driver.quit()


def test_instagram():
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(10)
    driver.quit()


def test_twitter():
    driver = webdriver.Chrome()
    driver.get('https://www.twitter.com/')
    driver.implicitly_wait(10)
    driver.quit()


@pytest.mark.fast
    def test_fast_test():
    number = 123
    assert number == 122