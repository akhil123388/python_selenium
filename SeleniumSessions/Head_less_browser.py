from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(5)
driver.get("http://amazon.in")
print(driver.title)