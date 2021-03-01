from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://amazon.in")
driver.find_element(By.LINK_TEXT, "Best Sellers").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
# driver.refresh()