from argparse import Action
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://google.com')


def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url == "https://www.google.com/"

def test_my_fast_test():
    assert "oogle" in driver.title





