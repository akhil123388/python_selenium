# using Firefox  (not working)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
profile=webdriver.FirefoxProfile()
profile.accept_untrusted_certs=True
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=profile)
driver.implicitly_wait(10)
driver.get("https://expired.badssl.com/")
print(driver.find_element(By.TAG_NAME,'h1').text)