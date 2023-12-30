import asyncio
import datetime
import hourObjFile
from env_canada import ECWeather
from env_canada import ECAirQuality

class Weather():
    
    def __init__(self, xCord = 0, yCord = 0) -> None:
        self.ec_en = ECWeather(coordinates=(xCord, yCord))
        self.ec_AQ = ECAirQuality(coordinates=(xCord, yCord))
        self.h = hourObjFile.hourObj()
        
    def get_weather_report(self) -> str:
        self.update_weather()
        # current temp
        self.tempDic = { 
            datetime.datetime.now().hour:self.ec_en.conditions["temperature"]["value"]
            }
        currentTemp = self.tempDic[datetime.datetime.now().hour]
        # daily forecasts
        currentMessage = self.ec_en.daily_forecasts[0]['text_summary']
        weatherReport = format("It is currently " + str(currentTemp) + "*C.\n" + 
                    currentMessage)
        
        return weatherReport

    def get_hourly_forecast(self) -> str:
        self.update_weather()
        hourlyForecast = "Hourly Forecast:"
        
        self.h.reset_hour()

        for info in self.ec_en.hourly_forecasts:
            hourlyForecast += "\n{}: {}*C, {}%, {}".format(str(self.h), info['temperature'], info['precip_probability'], info['condition'])
            self.h.increment()
            
        self.h.reset_hour()
        
        return hourlyForecast
    
    def get_AQHI_forecast(self) -> str:
        self.update_weather()

        daily_forecast_json = self.ec_AQ.forecasts.get('daily', {})
        
        # Check if daily forecast data is available
        if not daily_forecast_json:
            return "Daily forecast data not available."

        # Extract and format the daily forecast
        daily_forecast = "\n".join([f"{period}: {value}" for period, value in daily_forecast_json.items()])

        return f"Daily Forecast:\n{daily_forecast}"
        
    
    def update_weather(self):
        asyncio.run(self.ec_en.update())
        self.h.reset_hour()
        asyncio.run(self.ec_AQ.update())