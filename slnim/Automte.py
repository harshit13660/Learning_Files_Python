
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_argument('headless')
driver= webdriver.Chrome(executable_path="chromedriver.exe",options=options)

driver.get('https://www.youtube.com')
print(driver.title)
driver.find_element_by_id("search").send_keys('Rockstar song')
driver.implicitly_wait(3)
driver.find_element_by_class_name("style-scope ytd-thumbnail").click()

