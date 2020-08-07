from datetime import datetime

api_key = '73f5368224eb5dc6ab4b96b6cfaa24a7'
city_id = 6167865

url = f'api.openweathermap.org/data/2.5/forecast/hourly?id={city_id}&appid={api_key}'
t = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={api_key}'

five = f'api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={api_key}'
print(five)
