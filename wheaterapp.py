# What is JSON Parsing?
# JSON parsing = converting JSON data into Python objects (like dict/list) so we can use it in code.
# API gives data in JSON format (text)
# We use response.json() in Python to convert it to a dictionary
# Then we can access the values easily

# WITHOUT API KEY
# import requests

# def get_weather(city):
#     url =f"https://wttr.in/{city}?format=j1"   #?format=j1 → return the result in JSON format (machine-readable).
#     response = requests.get(url)

#     if response.status_code == 200:
#      data = response.json() #-->response is the obj we created earlier
#      current = data['current_condition'][0]
#      print(f"City: {city}")
#      print(f"Temperature: {current['temp_C']}°C")
#      print(f"Weather: {current['weatherDesc'][0]['value']}")
#      print(f"Humidity: {current['humidity']}%")
#     else:
#      print("Error fetching data!")

# city = input("Enter city name: ")
# get_weather(city)    



# WITH API KEY

import requests
 

def get_weather(city,api_key):
  base_url= "http://api.openweathermap.org/data/2.5/weather"


  params =  {
        "q" : city,
        "appid": api_key,
        "units" : "metric"  # use Celsius (use "imperial" for Fahrenheit)
      }
  response = requests.get(base_url , params=params)
        
   
  if response.status_code == 200:
      data = response.json()
      if data.get("cod") !=200:
       print("Error :",data.get("Unknown Error"))
      else:
       print(f"City:{data['name']}")
       print(f"Temperature:{data['main']['temp']}°C")  #main is nested dictionary inside data
       print(f"Weather:{data['weather'][0]['description']}")
       print(f"Humidity: {data['main']['humidity']}%")

  else:
    print("City not found!!")

api_key = "5554e226dc6fac63ce28b2316828da33"    
city= input("Enter the city name :").strip()
get_weather(city , api_key)
            
 # data['main']['temp'] → means:
# First go into the "main" section.
# Then grab the value of "temp".
# Example result → 29.5.
# 👉 That’s why we use main['temp'].
            