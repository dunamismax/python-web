"""State management for Weather App."""

import reflex as rx
import asyncio
from typing import List, Dict, Any, Optional
from .database import get_db_session, init_db
from .models import WeatherHistory, SavedLocation
from .weather_service import WeatherService

class WeatherState(rx.State):
    """State for managing weather data."""
    
    current_weather: Dict[str, Any] = {}
    forecast_data: List[Dict[str, Any]] = []
    saved_locations: List[Dict[str, Any]] = []
    search_city: str = ""
    is_loading: bool = False
    error_message: str = ""
    success_message: str = ""
    current_view: str = "current"  # current, forecast, history, locations
    weather_history: List[Dict[str, Any]] = []
    
    def __init__(self):
        super().__init__()
        self.weather_service = WeatherService()
        self.load_saved_locations()
        self.load_weather_history()
    
    def load_saved_locations(self):
        """Load saved locations from database."""
        try:
            init_db()
            db = get_db_session()
            locations = db.query(SavedLocation).order_by(SavedLocation.created_at.desc()).all()
            self.saved_locations = [location.to_dict() for location in locations]
            db.close()
        except Exception as e:
            self.error_message = f"Failed to load saved locations: {str(e)}"
    
    def load_weather_history(self):
        """Load weather history from database."""
        try:
            db = get_db_session()
            history = db.query(WeatherHistory).order_by(WeatherHistory.created_at.desc()).limit(20).all()
            self.weather_history = [record.to_dict() for record in history]
            db.close()
        except Exception as e:
            self.error_message = f"Failed to load weather history: {str(e)}"
    
    async def search_weather(self):
        """Search weather for a city."""
        if not self.search_city.strip():
            self.error_message = "Please enter a city name"
            return
        
        try:
            self.is_loading = True
            self.error_message = ""
            
            # Fetch current weather
            raw_data = await self.weather_service.get_current_weather(self.search_city.strip())
            weather_data = self.weather_service.parse_weather_data(raw_data)
            self.current_weather = weather_data
            
            # Save to history
            self.save_weather_to_history(weather_data)
            
            self.success_message = f"Weather data loaded for {weather_data['city']}"
            self.current_view = "current"
            
        except Exception as e:
            self.error_message = f"Failed to fetch weather: {str(e)}"
            self.current_weather = {}
        finally:
            self.is_loading = False
    
    async def get_forecast(self):
        """Get weather forecast for current city."""
        if not self.current_weather.get("city"):
            self.error_message = "Please search for a city first"
            return
        
        try:
            self.is_loading = True
            self.error_message = ""
            
            raw_forecast = await self.weather_service.get_forecast(self.current_weather["city"])
            
            # Parse forecast data (daily summary)
            daily_forecast = []
            for i in range(0, len(raw_forecast["list"]), 8):  # Every 8th item (daily)
                item = raw_forecast["list"][i]
                daily_data = {
                    "date": item["dt_txt"][:10],  # Extract date
                    "temperature": round(item["main"]["temp"], 1),
                    "feels_like": round(item["main"]["feels_like"], 1),
                    "humidity": item["main"]["humidity"],
                    "weather_main": item["weather"][0]["main"],
                    "weather_description": item["weather"][0]["description"].title(),
                    "icon": item["weather"][0]["icon"],
                    "wind_speed": item["wind"].get("speed", 0),
                }
                daily_forecast.append(daily_data)
            
            self.forecast_data = daily_forecast
            self.current_view = "forecast"
            self.success_message = f"Forecast loaded for {self.current_weather['city']}"
            
        except Exception as e:
            self.error_message = f"Failed to fetch forecast: {str(e)}"
            self.forecast_data = []
        finally:
            self.is_loading = False
    
    def save_weather_to_history(self, weather_data: Dict[str, Any]):
        """Save weather data to history."""
        try:
            db = get_db_session()
            
            history_record = WeatherHistory(
                city=weather_data["city"],
                country=weather_data["country"],
                temperature=weather_data["temperature"],
                feels_like=weather_data["feels_like"],
                humidity=weather_data["humidity"],
                pressure=weather_data["pressure"],
                wind_speed=weather_data["wind_speed"],
                wind_direction=weather_data["wind_direction"],
                weather_main=weather_data["weather_main"],
                weather_description=weather_data["weather_description"],
                icon=weather_data["icon"],
                timezone=weather_data["timezone"],
            )
            
            db.add(history_record)
            db.commit()
            
            # Reload history
            self.load_weather_history()
            
            db.close()
        except Exception as e:
            print(f"Failed to save weather history: {str(e)}")
    
    def save_current_location(self):
        """Save current weather location to saved locations."""
        if not self.current_weather.get("city"):
            self.error_message = "No current weather data to save"
            return
        
        try:
            db = get_db_session()
            
            # Check if location already exists
            existing = db.query(SavedLocation).filter(
                SavedLocation.city == self.current_weather["city"],
                SavedLocation.country == self.current_weather["country"]
            ).first()
            
            if existing:
                self.error_message = "Location already saved"
                db.close()
                return
            
            saved_location = SavedLocation(
                city=self.current_weather["city"],
                country=self.current_weather["country"],
                latitude=self.current_weather["latitude"],
                longitude=self.current_weather["longitude"],
                nickname=self.current_weather["city"],
            )
            
            db.add(saved_location)
            db.commit()
            
            self.load_saved_locations()
            self.success_message = f"Location {self.current_weather['city']} saved!"
            
            db.close()
        except Exception as e:
            self.error_message = f"Failed to save location: {str(e)}"
    
    def delete_saved_location(self, location_id: int):
        """Delete a saved location."""
        try:
            db = get_db_session()
            location = db.query(SavedLocation).filter(SavedLocation.id == location_id).first()
            
            if location:
                db.delete(location)
                db.commit()
                self.load_saved_locations()
                self.success_message = "Location deleted successfully!"
            
            db.close()
        except Exception as e:
            self.error_message = f"Failed to delete location: {str(e)}"
    
    async def load_weather_for_location(self, city: str):
        """Load weather for a saved location."""
        self.search_city = city
        await self.search_weather()
    
    def set_search_city(self, city: str):
        """Set search city."""
        self.search_city = city
        self.error_message = ""
    
    def set_current_view(self, view: str):
        """Set current view."""
        self.current_view = view
    
    def clear_messages(self):
        """Clear success and error messages."""
        self.success_message = ""
        self.error_message = ""
    
    @rx.var
    def has_current_weather(self) -> bool:
        """Check if current weather data exists."""
        return bool(self.current_weather.get("city"))
    
    @rx.var
    def weather_icon_url(self) -> str:
        """Get weather icon URL."""
        if self.current_weather.get("icon"):
            return self.weather_service.get_weather_icon_url(self.current_weather["icon"])
        return ""
    
    @rx.var
    def wind_direction_name(self) -> str:
        """Get wind direction name."""
        if self.current_weather.get("wind_direction"):
            return self.weather_service.get_wind_direction_name(self.current_weather["wind_direction"])
        return "N/A"