from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)    # find out title means
ele_indus = driver.find_element(By.ID, "Form_submitForm_Industry")
select = Select(ele_indus)
select.select_by_visible_text("Computer / Technology - Manufacturer")
# select.select_by_index(1)
# select.select_by_value("Business Services/Consultancy")
# print(select.is_multiple)
ele_country = driver.find_element(By.ID, "Form_submitForm_Country")
select=Select(ele_country)
select.select_by_visible_text("Angola")
