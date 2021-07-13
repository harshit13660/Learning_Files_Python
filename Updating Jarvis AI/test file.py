from tkinter import *
import os
import json
from tkinter import messagebox
from tkinter import filedialog
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from win32com.client import *
import requests as req
import xml.etree.ElementTree as et
from difflib import SequenceMatcher
import difflib
import io,zipfile
import time




def getting_appro_version():
    ver_from_site=[]
    information_parser = Dispatch("Scripting.FileSystemObject")
    version = information_parser.GetFileVersion("C:\Program Files\Google\Chrome\Application\chrome.exe")

    web_request = req.get('https://chromedriver.storage.googleapis.com')
    my_xml = et.fromstring(web_request.text)
    # namespace='http://doc.s3.amazonaws.com/2006-03-01'
    xml_contents=my_xml.findall('{http://doc.s3.amazonaws.com/2006-03-01}Contents')
    for i in xml_contents:
        ver_from_site.append((i.find('{http://doc.s3.amazonaws.com/2006-03-01}Key').text).split("/")[0])

    selected_version=difflib.get_close_matches(version,ver_from_site,1)
    ver_from_site.clear()
    return selected_version

def install_version():
    z="".join(getting_appro_version())
    qwe=req.get(f"https://chromedriver.storage.googleapis.com/{z}/chromedriver_win32.zip")
    z = zipfile.ZipFile((io.BytesIO(qwe.content)))
    z.extractall(os.getcwd())


def check_for_test_driver():
    global driver
    try:
        option=webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(executable_path='chromedriver.exe',options=option)
        driver.implicitly_wait(10)
        driver.get('https://www.google.com/')
        print("Driver is Ok ")
    except Exception as e:
        install_version()
        check_for_test_driver()

def chromedriver_kill(flag,driver):
    flag = flag
    while flag!=1:
        try:
            time.sleep(5)
            print(driver.title)
        except Exception as e:
            flag+=1
            os.system("TASKKILL /F /IM chromedriver.exe /T")



check_for_test_driver()


