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
def select_values(optionlist, values):
    for ele in optionlist:
        print(ele.text)
        for k in range(len(values)):
            if ele.text == values[k]:
                ele.click()
                break
list = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
list_value =["choice 6 1", "choice 6 2", "choice 6 2 1"]
select_values(list, list_value)
# select_values(list,"choice 2")







