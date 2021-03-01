from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.google.com")
    assert driver.title =="Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.facebook.com")
    assert driver.title =="Facebook – log in or sign up"
    driver.quit()

def test_Instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.instagram.com")
    assert driver.title =="Instagram"
    driver.quit()

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.gmail.com")
    assert driver.title =="Gmail"

    driver.quit()