import json
import requests
from tabulate import tabulate

endpointURL = 'https://api.weatherapi.com/v1/forecast.json?key=a4b36c3290e34a97aae133608220610&q=23.016062199507843,72.47214227178155'
apiResponse = requests.get(endpointURL).json()
# print(json.dumps(apiResponse, indent=4))

print(f'\n\nCurrent Weather Data:\n{json.dumps(apiResponse["current"], indent=4)}')

hourlyWeatherDataList = []
print(f'\n\nHourly Weather Forecast Data:')
for tempData in apiResponse["forecast"]["forecastday"]:
    for tempVal in tempData.get('hour'):
        hourlyWeatherDataList.append([tempVal["time"], tempVal["temp_c"], tempVal["wind_kph"], tempVal["wind_degree"], tempVal["pressure_mb"], tempVal["precip_mm"], tempVal["humidity"], tempVal["cloud"], tempVal["windchill_c"], tempVal["heatindex_c"], tempVal["dewpoint_c"], tempVal["chance_of_rain"], tempVal["chance_of_snow"], tempVal["vis_km"]])

print(tabulate(hourlyWeatherDataList, headers = ['TimeStamp', 'Temperature', 'Wind Speed', 'Wind Degree', 'Pressure', 'Precipitation', 'Humidity', 'Cloud', 'Wind Chill', 'Heat Index', 'Dew Point', 'Rain', 'Snow', 'Visibility'], tablefmt = 'psql'))
