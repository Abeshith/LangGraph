import requests

class WeatherForecastTools:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city: str) -> dict:
        """
        Get the current weather for a given city.
        """
        try: 
            url = f"{self.base_url}/weather"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        
        except Exception as e:
            print(f"Error fetching current weather: {e}")
            return {}
        
    def get_weather_forecast(self, place: str):
        """
        Get the weather forecast for a given place.
        """
        try:
            url = f"{self.base_url}/forecast"
            params = {
                'q': place,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        
        except Exception as e:
            print(f"Error fetching weather forecast: {e}")
            return {}
