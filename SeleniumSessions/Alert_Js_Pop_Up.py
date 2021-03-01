from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME, "proceed").click()
time.sleep(3)
# switching to pop up driver
alert=driver.switch_to.alert
print(alert.text)
driver.switch_to.default_content()    # driver coming to default page   
# alert.accept()  # click on ok
alert.dismiss()  # dismiss by escape button
# driver.find_element(By.NAME, "proceed").
# alert.send_keys("hi")

