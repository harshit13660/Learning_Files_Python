from selenium import webdriver

import time
import pyautogui
from pynput.mouse import Listener
from pynput import keyboard
from tkinter import Tk
import ast
import json

dict_actions={}

alt_pressed=None
keyboard_check_listner=None
alt_check_flag=0
chrome_options=webdriver.ChromeOptions()
chrome_options.add_extension('xpath-Finder.crx')
driver=webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options)

driver.get("https://www.cowin.gov.in/")



# get_xpath()



test()
