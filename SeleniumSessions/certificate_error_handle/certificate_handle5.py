from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# options = Options()
# options.add_argument("--allow-running-insecure-content")
# options.add_argument("--ignore-certificate-errors")
from webdriver_manager.firefox import GeckoDriverManager

desired_capabilities = DesiredCapabilities().FIREFOX.copy()
desired_capabilities["acceptInsecureCerts"]=True

driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(), desired_capabilities=desired_capabilities)
driver.implicitly_wait(10)
driver.get("https://expired.badssl.com/")
print(driver.find_element(By.TAG_NAME,'h1').text)