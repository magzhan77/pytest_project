from selenium import webdriver

def test_open_webpage():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the Pytest homepage
    driver.get("https://docs.pytest.org/en/latest/")

    # Check that the page title contains "pytest"
    assert "better" in driver.title

    # Close the browser window
    driver.quit()
