from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# chrome will tell  u that i will give u driver reference
# here is browser is launched
driver = webdriver.Chrome(executable_path="C:\\Users\\MVS AKHIL KUMAR\\Documents\\Drivers\\chromedriver.exe")
driver.implicitly_wait(10)
# launching some url
driver.get("http://www.google.com")
driver.find_element(By.NAME,'q').send_keys("naveen automationlabs")
optionlist = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionlist))
for ele in optionlist:
    print(ele.text)
    if ele.text == "naveen automationlabs youtube":
        ele.click()
        break

# print title of page
print(driver.title)
time.sleep(10)
driver.quit()
