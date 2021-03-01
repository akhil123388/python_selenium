from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName = "firefox"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.safari()
else:
    print("please correct tne browser name:" + browserName)
    raise Exception("driver is not found")
driver.get("http://app.hubspot.com/login")
driver.implicitly_wait(10)

driver.find_element(By.ID, 'username').send_keys("mvsakhil@gmail.com")
driver.find_element(By.ID, 'password').send_keys("test@123")
driver.find_element(By.ID, 'loginBtn').click()
print(driver.title)
time.sleep(2)
driver.quit()




