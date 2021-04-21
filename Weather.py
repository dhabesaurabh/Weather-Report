import requests, json

api_key = "7ff4bfc106a1c3dacb55a55a69641cbb"

url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name : ")

new_url = url + "appid=" + api_key + "&q=" + city

response = requests.get(new_url)

if response.status_code != 404:
   data = response.json()
   main = data['main']
   temperature = main['temp']
   #temp_celsius = temperature-273.15
   print("Temperature in ", city, " is ", temperature, " °F.")

else:
   print("Invalid city name or temperature not found...")