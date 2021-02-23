from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
driver = None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

    yield
    driver.quit()

def test_google_title(init_driver):
    assert driver.title == "Google"

def test_google_url(init_driver):
    assert driver.current_url =="https://www.google.com/"




# other way

@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url =="https://www.google.com/"




