import requests

# WeatherAPI key
WEATHER_API_KEY = 'd603d4cd0eb74fc1af3193710260902'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    base_url = "http://api.weatherapi.com/v1/current.json"
    url = f"{base_url}?key={WEATHER_API_KEY}&q={city}"
    
    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful. 
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found). 
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information: 
        data = response.json()
        current = data['current']
        location = data['location']

        # - Current temperature in Fahrenheit 
        temp_f = current['temp_f']
        # - The "feels like" temperature 
        feelslike_f = current['feelslike_f']
        # - Weather condition (e.g., sunny, cloudy, rainy) 
        condition = current['condition']['text']
        # - Humidity percentage 
        humidity = current['humidity']
        # - Wind speed and direction 
        wind_mph = current['wind_mph']
        wind_dir = current['wind_dir']
        # - Atmospheric pressure in mb 
        pressure_mb = current['pressure_mb']
        # - UV Index value [cite: 110]
        uv = current['uv']
        # - Cloud cover percentage 
        cloud = current['cloud']
        # - Visibility in miles
        vis_miles = current['vis_miles']

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"\nWeather data for {location['name']}, {location['region']}:")
        print(f"Status 200: OK")
        print(f"Temperature: {temp_f}°F (Feels like: {feelslike_f}°F)")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind_mph} mph, Direction: {wind_dir}")
        print(f"Pressure: {pressure_mb} mb")
        print(f"UV Index: {uv}")
        print(f"Cloud Cover: {cloud}%")
        print(f"Visibility: {vis_miles} miles")
    else:
        # TODO: Implement error handling for common status codes.
        if response.status_code == 400:
            print(f"Error 400: Bad Request. Please check the city name.")
        elif response.status_code == 401:
            print(f"Error 401: Unauthorized. Check your API key.")
        elif response.status_code == 404:
            print(f"Error 404: Not Found. Resource not located.")
        else:
            print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    user_city = input("Enter city name: ")
    
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(user_city)
