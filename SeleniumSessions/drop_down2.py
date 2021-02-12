from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)

ele_country = driver.find_element(By.ID, "Form_submitForm_Country")
ele_indus = driver.find_element(By.ID, "Form_submitForm_Industry")

select_values(ele_indus,"Aerospace")
select_values(ele_country,"Afghanistan")