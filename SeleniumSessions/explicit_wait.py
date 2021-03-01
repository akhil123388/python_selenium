from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')

wait = WebDriverWait(driver, 10)
email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))
email_id.send_keys('a@gmail.com')
