from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME,"proceed").click()
alert=wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()