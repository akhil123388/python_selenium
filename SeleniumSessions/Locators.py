from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)    # find out title means
# driver.find_element(By.ID, "Form_submitForm_subdomain").send_keys("akhil_url")
user_ele = driver.find_element(By.ID, "Form_submitForm_subdomain")
user_ele.send_keys("akhil_url")

first_name = driver.find_element(By.ID, "Form_submitForm_FirstName")
last_name = driver.find_element(By.ID, "Form_submitForm_LastName")
email = driver.find_element(By.ID, "Form_submitForm_Email")
feature = driver.find_element(By.LINK_TEXT, "Features")
first_name.send_keys("mvs")
last_name.send_keys("akhil")
email.send_keys("akhil@gmail.com")
feature.click()





