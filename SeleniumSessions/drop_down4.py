# with out select cls
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)    # find out title means
ele_indus_list = driver.find_elements(By.XPATH, "//select[@id='Form_submitForm_Industry']/option")
print(len(ele_indus_list))
for ele in ele_indus_list:
    print(ele.text)
    if ele.text == "Travel":
        ele.click()
        break