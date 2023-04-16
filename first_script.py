import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    # Initialize a Chrome browser instance
    driver = webdriver.Chrome()
    yield driver
    # Teardown: close the browser

def test_google_search(browser):
    # Navigate to the Google homepage
    browser.get('https://www.google.com/')
    # Find the search input element
    search_box = browser.find_element(By.NAME, 'q')
    # Type a search query
    search_box.send_keys('pytest with selenium')
    # Press enter
    search_box.send_keys(Keys.RETURN)
    # Wait for the search results to load
    browser.implicitly_wait(10)
    # Verify the page title contains the search query
    assert 'pytest with selenium' in browser.title
    assert 'selenium' in browser.current_url