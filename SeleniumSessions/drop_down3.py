from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)    # find out title means
ele_indus = driver.find_element(By.ID, "Form_submitForm_Industry")
select=Select(ele_indus)
ele_indus_List = select.options
for ele in ele_indus_List:
    print(ele.text)
    if(ele.text == 'Automotive'):
        ele.click()
        break
