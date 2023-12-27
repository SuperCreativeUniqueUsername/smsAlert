import asyncio
import datetime
import hourObjFile
from env_canada import ECWeather

class Weather():
    
    def __init__(self, xCord = 0, yCord = 0) -> None:
        self.ec_en = ECWeather(coordinates=(xCord, yCord))
        self.days = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }
        asyncio.run(self.ec_en.update())
        self.tempDic = { 
            datetime.datetime.now().hour:self.ec_en.conditions["temperature"]["value"]
            }
        self.h = hourObjFile.hourObj()
        
    def get_weather_report(self):
        # current temp
        currentTemp = self.tempDic[datetime.datetime.now().hour]
        # daily forecasts
        currentMessage = self.ec_en.daily_forecasts[0]['text_summary']
        weatherReport = format("It is currently " + str(currentTemp) + "*C.\n" + 
                    currentMessage + "\n\n" +
                    "Hourly Forecast:")

        self.h.reset_hour()

        for info in self.ec_en.hourly_forecasts:
            weatherReport += "\n{}: {}*C, {}%, {}".format(str(h), info['temperature'], info['precip_probability'], info['condition'])
            self.h.increment()
            
        self.h.reset_hour()
        
        return weatherReport
    
    def update_weather(self):
        asyncio.run(self.ec_en.update())
        self.tempDic = { 
            datetime.datetime.now().hour:self.ec_en.conditions["temperature"]["value"]
            }
        self.h.reset_hour()