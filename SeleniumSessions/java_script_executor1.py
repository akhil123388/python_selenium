from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://amazon.in")
best_seller = driver.find_element(By.LINK_TEXT, "Best Sellers")

print(driver.execute_script("return document.documentElement.innerText;"))
driver.execute_script("arguments[0].style.border='3px solid red'",best_seller)
