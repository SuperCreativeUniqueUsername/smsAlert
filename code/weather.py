import asyncio
import datetime

from env_canada import ECWeather

ec_en = ECWeather()

asyncio.run(ec_en.update())

days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

tempdic = { 
    datetime.datetime.now().hour:ec_en.conditions["temperature"]["value"]
    }

print(tempdic[datetime.datetime.now().hour])

# daily forecasts
print(ec_en.daily_forecasts[0]['text_summary'])

# hourly forecasts
'''
for i in ec_en.hourly_forecasts:
    print(i['temperature'])'''
