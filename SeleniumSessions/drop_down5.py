# with out select cls using generic function
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
def select_values_drop_down_list(drop_down_list,value):
    print(len(ele_indus_list))
    for ele in ele_indus_list:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

ele_indus_list = driver.find_elements(By.XPATH, "//select[@id='Form_submitForm_Industry']/option")
select_values_drop_down_list(ele_indus_list, "Electronics")
select_values_drop_down_list(ele_indus_list, "Travel")


