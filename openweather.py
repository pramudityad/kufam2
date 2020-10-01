import requests
import json
import datetime

api_key = "ed7a5356f1bf92e60f84aca931330450"
# lenteng agung
lat = "-6.331487"
lon = "106.835068"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

rain_code = [200,201,202,210,211,212,221,230,231,232,500,501,502,503,504,511,520,521,522,531,600,601,602,611,612,613,615,616,620,621,622]
clouds_code = [801,	801,801,801,701,711,721,731,741,751,761,762,771,781]


response = requests.get(url)
data = json.loads(response.text)

def today_sunset_sunrise():
	currents = data["current"]
	sunrise = datetime.datetime.fromtimestamp(currents["sunrise"])
	sunset = datetime.datetime.fromtimestamp(currents["sunset"])
	return sunrise, sunset

def today_weather():
	weathers = data["current"]["weather"]
	for entry in weathers:
		weather = entry["main"]
		code_id = entry["id"]
		if code_id in rain_code:
			code = 2
		if code_id in clouds_code:
			code = 1
		else:
			code = 0
		return code

def hourly_weather():    
    weathers = data["hourly"]
    for entry in weathers:
        time = datetime.datetime.fromtimestamp(entry["dt"])
        temp = entry["temp"]
        hum = entry["humidity"]		