from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://amazon.in")
best_seller = driver.find_element(By.LINK_TEXT, "Best Sellers")
# how to click this best_seller through java script executor
driver.execute_script("arguments[0].click();", best_seller)
title=driver.execute_script("return document.title;")
print(title)
driver.execute_script("history.go(0);")
# driver.execute_script("alert('hello');")
print(driver.execute_script("return document.documentElement.innerText;"))
# it wont work for best seller bec it doesnot have innertext