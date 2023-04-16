import pytest
@pytest.fixture
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()

def test_search(browser):
    browser.get("https://docs.pytest.org/en/latest/")

    search_box = browser.find_element_by_name("q")

    search_box.send_keys("fixtures")

    search_box.submit()

    assert "fixtures" in browser.title