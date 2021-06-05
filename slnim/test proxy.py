from pushbullet import Pushbullet
import time
import requests
import datetime

b=datetime.datetime.today()
url="https://api.ipify.org/?format=json"
#
# API= 'o.WfYU9eM5o7fXoBq5PxburlwjXEpfCw0Q'
# pb=Pushbullet(API)

header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

proxi={
    "https": "14.140.131.82:3128",
    "http" : "14.140.131.82:3128"
}
para={"district_id": 148, "date": b.strftime("%d-%m-%Y")}

try:
    re=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?",params=para,proxies=proxi,headers=header)
    print(re)
except Exception as e:
    print("Failed Trying Again")


try:
    a=requests.get(url,proxies=proxi).json()
    print(a)
except Exception as e:
    print("Exception")
