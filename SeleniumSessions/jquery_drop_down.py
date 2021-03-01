from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)
driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(2)
list = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
for ele in list:
    print(ele.text)
    if ele.text == "choice 2 2":
        ele.click()
        break



