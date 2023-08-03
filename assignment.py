import requests

def get_weather_data(location):
    api_key = "b6907d289e10d714a6e88b30761fae22"
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving weather data.")
        return None

def get_weather_info(weather_data, date):
    weather_info = []
    for forecast in weather_data['list']:
        if forecast['dt_txt'].split()[0] == date:
            weather_info.append({
                'time': forecast['dt_txt'].split()[1],
                'temperature': forecast['main']['temp'],
                'wind_speed': forecast['wind']['speed'],
                'pressure': forecast['main']['pressure']
            })
    return weather_info

def main():
    location = "London,us"
    weather_data = get_weather_data(location)
    if not weather_data:
        return

    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            weather_info = get_weather_info(weather_data, date)
            if weather_info:
                print(f"Weather info for {date}:")
                for data in weather_info:
                    print(f"Time: {data['time']} | Temperature: {data['temperature']}°C")
            else:
                print("Weather data not available for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            weather_info = get_weather_info(weather_data, date)
            if weather_info:
                print(f"Wind Speed on {date}:")
                for data in weather_info:
                    print(f"Time: {data['time']} | Wind Speed: {data['wind_speed']} m/s")
            else:
                print("Weather data not available for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            weather_info = get_weather_info(weather_data, date)
            if weather_info:
                print(f"Pressure on {date}:")
                for data in weather_info:
                    print(f"Time: {data['time']} | Pressure: {data['pressure']} hPa")
            else:
                print("Weather data not available for the given date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
