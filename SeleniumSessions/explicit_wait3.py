# element to be clickable
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 30)
driver.get("https://app.hubspot.com/login")
sign_up=wait.until(ec.element_to_be_clickable((By.LINK_TEXT,"Sign up")))
print(sign_up.text)