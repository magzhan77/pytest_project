import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = None

def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://google.com/')
    assert driver.title == "Google"
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://facebook.com/')
    assert driver.title == "Facebook — Выполните вход или зарегистрируйтесь"
    driver.quit()


def test_insta():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://instagram.com/')
    assert driver.title == "Instagram"
    driver.quit()
