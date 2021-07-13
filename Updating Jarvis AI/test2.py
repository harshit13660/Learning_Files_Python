from bs4 import BeautifulSoup

# Importing the HTTP library
import requests as req
import xml.etree.ElementTree as et


web = req.get('https://chromedriver.storage.googleapis.com')
mytree = et.fromstring(web.text)
nsp='http://doc.s3.amazonaws.com/2006-03-01'
ele=mytree.findall('{http://doc.s3.amazonaws.com/2006-03-01}Contents')
for i in ele:
    version=i.find('{http://doc.s3.amazonaws.com/2006-03-01}Key').text

