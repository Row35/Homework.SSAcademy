import pyowm

owm = pyowm.OWM('b4c3afe8b6b5d2afab3cefc8da5d1f20')  # You MUST provide a valid API key
# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

###########################################################################
place = input("please, enter in which city do you want to check weather: ")
###########################################################################

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>
                              # Weather details
wind = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
humidity = w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
x=float(input("Enter the longitude: "))
y=float(input("Enter the latitude: "))
observation_list = owm.weather_around_coords(x, y)

print("In city " + place + " now is " + w.get_detailed_status()) 
print('Temperature there is: ' + str(temp) + '°C')
print ('Wind speed there is: '+ str(wind["speed"]))
print ("In city " + place + "the humidity now is " + str(humidity))

################  additionaly ##########################################

# w = observation.get_weather()
# print (w)                     
# print " Weather details"
# print " =============== "
                                    
# print " Get cloud coverage"
# print w.get_clouds() 
# print " ----------------"                                     
# print " Get rain volume"
# print w.get_rain() 
# print " ----------------"
# print " Get snow volume"
# print w.get_snow()                                       

# print " Get wind degree and speed"
# print w.get_wind() 
# print " ----------------"                                      
# print " Get humidity percentage"
# print w.get_humidity()    
# print " ----------------"                               
# print " Get atmospheric pressure"
# print w.get_pressure()                                   
# print " ----------------"
# print " Get temperature in Kelvin degs"
# print w.get_temperature() 
# print " ----------------"                              
# print " Get temperature in Celsius degs"
# print w.get_temperature(unit='celsius')
# print " ----------------"                 
# print " Get temperature in Fahrenheit degs"
# print w.get_temperature('fahrenheit')                    
# print " ----------------"
# print " Get weather short status"
# print w.get_status()                                     
# print " ----------------"
# print " Get detailed weather status"
# print w.get_detailed_status()                           
# print " ----------------"
# print " Get OWM weather condition code"
# print w.get_weather_code()                               
# print " ----------------"
# print " Get weather-related icon name"
# print w.get_weather_icon_name()                          
# print " ----------------"
# print " Sunrise time (ISO 8601)"
# print w.get_sunrise_time('iso')    
# print " Sunrise time (GMT UNIXtime)"
# print w.get_sunrise_time()                               
# print " ----------------"
# print " Sunset time (ISO 8601)"
# print w.get_sunset_time('iso')  
# print " Sunset time (GMT UNIXtime)"
# print w.get_sunset_time()                          
# print " ----------------"
# print " Search current weather observations in the surroundings of"
# print " Latitude and longitude coordinates"+place
# observation_list = owm.weather_around_coords(lon, lat)




