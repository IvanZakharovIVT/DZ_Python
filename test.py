import pyowm
import wikipedia

owm = pyowm.OWM(API_key = 'ea10913f4eb6164d64ed6bab222667da',
	language='ru')

ms = input("Введите город ")
try:
	observation = owm.weather_at_place(ms)
	w = observation.get_weather()
	print(w)
	print(w.get_wind())
	print(w.get_humidity())
	print("Температура " + str(w.get_temperature('celsius')['temp']))
	print(w.get_detailed_status())
	#Легкий/_/Cbkmysq дождь/ Ясно/пасмурно/облачно (eng)
	print(w.get_status())
	#Rain Clouds Clear
	print(observation.get_reception_time(timeformat='iso'))
	print(w.get_rain())
	wikipedia.set_lang("ru")  
	print(wikipedia.summary(ms))
except Exception:
	print("Я не знаю такого города")