import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    # Open the browser
    driver = webdriver.Chrome()
    yield driver
    # Close the browser
    driver.quit()

def test_search_google(browser):
    # Navigate to Google
    browser.get('https://www.google.com')
    # Find the search box and enter a query
    search_box = browser.find_element(By.CLASS_NAME, 'q')
    search_box.send_keys('Selenium pytest')
    search_box.send_keys(Keys.ENTER)
    # Verify the search results
    assert 'pytest' in browser.title