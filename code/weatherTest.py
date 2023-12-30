
import asyncio

from env_canada import ECAirQuality

aqhi_coords = ECAirQuality(coordinates=(0, -0))

asyncio.run(aqhi_coords.update())

# Data available
#print(aqhi_coords.current)
daily_forecast = aqhi_coords.forecasts.get('daily', {})

# Print out the daily forecast in a nice format
daily_forecast_string = format("Daily Forecast:\n" + 
                               "\n".join([f"{period}: {value}" for period, value in daily_forecast.items()]))
print(daily_forecast_string)