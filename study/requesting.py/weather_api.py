import requests
import json
import datetime

API_KEY = '73f5368224eb5dc6ab4b96b6cfaa24a7'
CITY_ID = 6167865

url = f'http://api.openweathermap.org/data/2.5/forecast?id={CITY_ID}&appid={API_KEY}'
r = requests.get(url)
data_json = r.json()
data_str = json.dumps(data_json['list'][0], indent=2)
most_recent = data_json['list'][0]
print(data_str)

dt = most_recent.get('dt')  # epoch datetime
dt = datetime.datetime.fromtimestamp(dt).strftime('%c')  # converted datetime

feels_k = most_recent.get('main').get('feels_like')  # feels like in Kelvin
feels_c = round(feels_k - 273.15, 1)
w_descript = most_recent.get('weather')[0].get('description')
pop = most_recent.get('pop')
rain = most_recent.get('rain')
if rain is not None:
    rain = rain.get('3h')

print()
print(dt)
print(feels_c)
print(w_descript)
print(pop)
print(rain)
