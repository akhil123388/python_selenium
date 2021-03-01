from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
# options.add_argument("--allow-running-insecure-content")
# options.add_argument("--ignore-certificate-errors")
options.set_capability("acceptInsecureCerts",True)


driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
driver.implicitly_wait(10)
driver.get("https://expired.badssl.com/")
print(driver.find_element(By.TAG_NAME,'h1').text)