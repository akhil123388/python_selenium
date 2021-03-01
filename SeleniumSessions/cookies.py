
# some website data which defines to help you certain data whenever you are gng to load the page see what type of domain
# u have nd what type of language u have
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)       
driver.get("https://www.reddit.com")
# print(driver.get_cookies().__len__())
# print(driver.get_cookies())

# how to add cookies
driver.add_cookie({'name': 'Akhil', 'domain': 'reddit.com', 'value': 'new_cookie'})
cookies=driver.get_cookies()
for cook in cookies:
    print(cook)
