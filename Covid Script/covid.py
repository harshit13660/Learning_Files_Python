import requests
from datetime import datetime
from pushbullet import PushBullet
import time
from selenium import webdriver

def Registr():
    driver= webdriver.Chrome(executable_path="C:\\Users\Harshit\PycharmProjects\slnim\chromedriver.exe")
    driver.get('https://www.cowin.gov.in/home')
    driver.find_element_by_xpath("//*[@id='navbarTogglerDemo01']/ul/li[5]/a").click()



API_har= 'o.WfYU9eM5o7fXoBq5PxburlwjXEpfCw0Q'
pb_har=PushBullet(API_har)
print(pb_har)

#SHAHDARA
b=datetime.today()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?'

para={"district_id": 145, "date": b.strftime("%d-%m-%Y")}

# proxi={
#     "https": "http://14.140.131.82:3128",
#     "http" : "http://139.5.19.165:8080"
# }

while True:
    count = 0
    try:
        a=requests.get(url,params=para,headers=headers )
        file = a.json()

        for i in range(0, len(file['centers'])):
            if(file['centers'][i]['sessions'][0]['min_age_limit'] == 45 and (file['centers'][i]['sessions'][0]['available_capacity_dose1'] >= 1)):
                count = count + 1

        if count >= 1:
            pb_har.push_note("Vaccine Slots Available", "Slots Available for 18+ Hurry up")
        print("Successfully entered try block")

    except Exception as e:
        print(e)










