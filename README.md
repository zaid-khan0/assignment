# Weather Forecast Program

This is a Python program that interacts with the OpenWeatherMap API to provide weather forecast data for a specific location. 
The program allows users to query and retrieve weather-related information based on their choices.

# Requirements

Python 3
'requests' library (install using 'pip install requests')

# How to Use

Clone the repository to your local machine.
Ensure you have Python 3 installed on your system.
Install the required 'requests' library by running the following command:

    '''
    pip install requests
    '''

Run the program using the following command:

    '''
    python weather_forecast.py
    '''

The program will prompt you with a menu of options:

Menu:

Get weather
Get Wind Speed
Get Pressure


6. Choose the option based on your preference:

If you choose "Get weather," you will be prompted to enter a date (YYYY-MM-DD). The program will then retrieve and display the temperature for the given date.

If you choose "Get Wind Speed," you will be prompted to enter a date (YYYY-MM-DD). The program will then retrieve and display the wind speed for the given date.

If you choose "Get Pressure," you will be prompted to enter a date (YYYY-MM-DD). The program will then retrieve and display the atmospheric pressure for the given date.

If you choose "Exit," the program will terminate.

The program will continue running until you choose the "Exit" option.

# API Information

The program uses the OpenWeatherMap API to fetch hourly weather forecast data for a specific location (London, US) in JSON format. The API endpoint used in the program is:

https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22

