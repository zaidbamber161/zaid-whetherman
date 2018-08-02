import sys
import collections

pkt = '2014-03-26'
max_temperature = 23
mean_temperature = 0
min_temperature = 21
dew_point = 17
mean_dew_point = 17
min_dew_point = 16
max_humidity = 14
mean_humidity = 14
min_humidity = 83
max_sea_level_pressure = 0
mean_sea_level_pressure = 0
min_sea_level_pressure = 0
max_visibility = 0.0
mean_visibility = 0.0
min_visibility = 0.0
max_wind_speed = 0
mean_wind_speed = 0
max_gust_speed = 0
precipitation = 0.0
cloudCover = 0
events = "wind"
wind_dir_degrees = -1

# weather_reading = [pkt[0], max_temperature[0] + max_temperature[1], mean_temperature]

# print(weather_reading)
# print(max_temperature)
#text = input("prompt")  


weather_report = []

year_month = []

daily_results = []

weather_reading1 = []


keys = ['pkt', 'max_temperature', 'mean_temperature','min_temperature','dew_point','mean_dew_point'
        ,'min_dew_point','max_humidity','mean_humidity','min_humidity','max_sea_level_pressure',
        'mean_sea_level_pressure','min_sea_level_pressure','max_visibility','mean_visibility',
        'min_visibility','max_wind_speed','mean_wind_speed','max_gust_speed','precipitation',
        'cloudCover','events','wind_dir_degrees']


day1 = [pkt,max_temperature ,mean_temperature,min_temperature,dew_point,mean_dew_point,
min_dew_point,max_humidity,mean_humidity,min_humidity,max_sea_level_pressure,
mean_sea_level_pressure,min_sea_level_pressure,max_visibility,mean_visibility,min_visibility,
max_wind_speed,mean_wind_speed,max_gust_speed,precipitation,cloudCover,events,wind_dir_degrees]
 
daily_results.append(day1)
daily_results.append(day1)


daily_list = []

daily_list.append(dict(zip(keys,day1)))
# daily_list.append(dict(zip(keys,day2)))



# print(daily_list)


print(daily_results)