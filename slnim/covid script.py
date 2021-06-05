import requests
from datetime import datetime
from pushbullet import PushBullet
import time



API_har= 'o.WfYU9eM5o7fXoBq5PxburlwjXEpfCw0Q'
pb_har=PushBullet(API_har)

API_tos= "o.2qGnwMYbBQd8nmf7AcKcNz1Zk7V4VABD"
pb_tos=PushBullet(API_tos)

#SHAHDARA
b=datetime.today()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?'

para={"district_id": 148, "date": b.strftime("%d-%m-%Y")}

proxi={
    "https": "http://14.140.131.82:3128",
    "http" : "http://139.5.19.165:8080"
}

while True:
    count = 0
    try:
        a=requests.get(url,params=para,headers=headers,proxies=proxi)
        file = a.json()

        for i in range(0, len(file['centers'])):
            if(file['centers'][i]['sessions'][0]['min_age_limit'] == 45 and (file['centers'][i]['sessions'][0]['available_capacity'] >= 1)):
                count = count + 1

        if count >= 1:
            pb_har.push_note("Vaccine Slots Available", "Slots Available for 18+ Hurry up")
            pb_tos.push_note("Vaccine Slots Available", "Slots Available for 18+ Hurry up")

    except Exception as e:
        print(e)

    time.sleep(5)









