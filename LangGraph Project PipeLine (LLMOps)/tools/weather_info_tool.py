import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from utils.weather_info import WeatherForecastTools

from langchain.tools import tool

class WeatherInfoTool:
    def __init__(self):
        load_dotenv
        self.api_key = os.environ.get("WEATHER_API_KEY")
        self.weather_service = WeatherForecastTools(self.api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        @tool
        def get_current_weather(city: str) -> str:
            """
            Get the current weather for a given city.
            """
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get('main', {}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                return f"The current temperature in {city} is {temp}°C with {desc}."
            return f"Could not retrieve weather data for {city}."
        
        @tool
        def get_weather_forecast(city: str, days: int = 5) -> str:
            """
            Get the weather forecast for a given city for the next few days.
            """
            forecast_data = self.weather_service.get_weather_forecast(city, days)
            if forecast_data and 'list' in forecast_data:
                forecast = []
                for day in forecast_data['list']:
                    date = day['dt_txt'].split(" ")[0] 
                    temp = day['main']['temp']
                    desc = day['weather'][0]['description']
                    forecast.append(f"{date}: {temp}°C, {desc}")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast)
            return f"Could not retrieve weather forecast for {city}."
        
        return [get_current_weather, get_weather_forecast]
                