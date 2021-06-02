import requests, json
  
api_key = "6fb346b973f68ff543c00d1172998dff"
  
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
city_name = input("Enter city name : ")
  
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  

response = requests.get(complete_url)

print(response)  

x = response.json()

print(x) 

if x["cod"] != "404":

    y = x["main"]
  

    current_temperature = y["temp"]
  

    current_pressure = y["pressure"]
  
    current_humidiy = y["humidity"]
  
    z = x["weather"]
  
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
    weather_description = z[0]["description"]
  
    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))
  
else:
    print(" City Not Found ")