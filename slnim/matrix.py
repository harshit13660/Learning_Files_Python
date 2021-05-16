from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("headless")
options.get_network_conditions()
browse = webdriver.Chrome(executable_path="chromedriver.exe",options=options)
browse.get("https://www.google.com")
print(browse.title)

