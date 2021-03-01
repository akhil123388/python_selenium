from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(5)
driver.get("https://www.reddit.com")
# driver.get_screenshot_as_file("reddit_1.png")

'''full screenshot'''
S=lambda X:driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S("Height"))
driver.find_element_by_tag_name("body").screenshot('reddit_ful.png');