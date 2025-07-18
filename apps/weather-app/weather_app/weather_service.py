"""Weather service for OpenWeatherMap API integration."""

import httpx
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

class WeatherService:
    """Service for fetching weather data from OpenWeatherMap API."""
    
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5"
        
    async def get_current_weather(self, city: str) -> Dict[str, Any]:
        """Get current weather for a city."""
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY environment variable.")
        
        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    
    async def get_weather_by_coordinates(self, lat: float, lon: float) -> Dict[str, Any]:
        """Get current weather by coordinates."""
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY environment variable.")
        
        url = f"{self.base_url}/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    
    async def get_forecast(self, city: str, days: int = 5) -> Dict[str, Any]:
        """Get weather forecast for a city."""
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY environment variable.")
        
        url = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "cnt": days * 8  # 8 forecasts per day (every 3 hours)
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    
    def parse_weather_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse OpenWeatherMap API response into clean format."""
        try:
            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"]["feels_like"], 1),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"].get("speed", 0),
                "wind_direction": data["wind"].get("deg", 0),
                "weather_main": data["weather"][0]["main"],
                "weather_description": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"],
                "timezone": data["timezone"],
                "latitude": data["coord"]["lat"],
                "longitude": data["coord"]["lon"],
            }
        except KeyError as e:
            raise ValueError(f"Invalid weather data format: missing {e}")
    
    def get_weather_icon_url(self, icon: str) -> str:
        """Get URL for weather icon."""
        return f"https://openweathermap.org/img/wn/{icon}@2x.png"
    
    def get_wind_direction_name(self, degrees: int) -> str:
        """Convert wind direction degrees to compass direction."""
        directions = [
            "N", "NNE", "NE", "ENE",
            "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW",
            "W", "WNW", "NW", "NNW"
        ]
        
        index = round(degrees / 22.5) % 16
        return directions[index]