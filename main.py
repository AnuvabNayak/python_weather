import requests, json
 
API_KEY = 'bda19833e22bf1216527e241dbbc7e5e'
 
def fetch_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}"
    response = requests.get(complete_url)
    return response.json()
 
def display_weather_data(weather_data):
    if weather_data['cod'] != '404':
        main_data = weather_data['main']
        wind_data = weather_data['wind']
        
        # Convert from Kelvin to Celsius
        temperature = main_data['temp'] - 273.15
         
        wind_speed = wind_data['speed']
        pressure = main_data['pressure']
        weather_description = weather_data['weather'][0]['description']
 
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Wind_Speed: {wind_speed}km/h")
        print(f"Pressure: {pressure} millibars")
        print(f"Weather description: {weather_description.capitalize()}")
 
    else:
        print("City not found. Please try again.")
 
def main():
    city = input("Enter the name of the city: ")
    weather_data = fetch_weather_data(city)
    display_weather_data(weather_data)  
    
if __name__ == "__main__":
    main()