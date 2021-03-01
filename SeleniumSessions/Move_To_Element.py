from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.spicejet.com")
time.sleep(3)
'''move to element'''
login_ele = driver.find_element(By.ID,'ctl00_HyperLinkLogin')
act_chains = ActionChains(driver)
act_chains.move_to_element(login_ele).perform()

spice_club_ele = driver.find_element(By.LINK_TEXT,'SpiceClub Members')
act_chains.move_to_element(spice_club_ele).perform()
member_login_ele = driver.find_element(By.LINK_TEXT,'Member Login')
member_login_ele.click()














































