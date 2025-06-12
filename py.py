import requests 

API = "05d508fe5fcc6829f2913e4537d4d6b8"
baseUrl = "https://api.openweathermap.org/data/2.5/weather"

def getWeatherInfo(cityName):
    url = f"{baseUrl}?q={cityName}&appid={API}"
    response= requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        print("Error: Unable to fetch weather data.")

cityName = input("Enter the city name: ")
weather_info = getWeatherInfo(cityName)

if weather_info:
    print("Weather Information:")
    print(f"City: {weather_info['name']}")
    print(f"Temperature: {weather_info['main']['temp']} K")
    print(f"Weather: {weather_info['weather'][0]['description']}")