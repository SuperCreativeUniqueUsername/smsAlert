import asyncio

from env_canada import ECWeather

ec_en = ECWeather(coordinates=(50, -100))

asyncio.run(ec_en.update())

# alerts
#print(ec_en.alerts)
# print(ec_en.daily_forecasts)

import asyncio

from env_canada import ECAirQuality

aqhi_coords = ECAirQuality(coordinates=(50, -100))

asyncio.run(aqhi_coords.update())

# Data available
#print(aqhi_coords.current)
print(aqhi_coords.forecasts)