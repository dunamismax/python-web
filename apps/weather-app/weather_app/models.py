"""Database models for the Weather App."""

from sqlalchemy import Column, String, Float, Integer, Text
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../packages"))
from shared.database import BaseModel

class WeatherHistory(BaseModel):
    """Weather history model for storing past weather queries."""
    __tablename__ = "weather_history"
    
    city = Column(String(100), nullable=False)
    country = Column(String(50), nullable=True)
    temperature = Column(Float, nullable=False)
    feels_like = Column(Float, nullable=True)
    humidity = Column(Integer, nullable=True)
    pressure = Column(Integer, nullable=True)
    wind_speed = Column(Float, nullable=True)
    wind_direction = Column(Integer, nullable=True)
    weather_main = Column(String(50), nullable=False)
    weather_description = Column(String(200), nullable=False)
    icon = Column(String(10), nullable=True)
    timezone = Column(Integer, nullable=True)
    
    def to_dict(self):
        """Convert weather record to dictionary."""
        return {
            "id": self.id,
            "city": self.city,
            "country": self.country,
            "temperature": self.temperature,
            "feels_like": self.feels_like,
            "humidity": self.humidity,
            "pressure": self.pressure,
            "wind_speed": self.wind_speed,
            "wind_direction": self.wind_direction,
            "weather_main": self.weather_main,
            "weather_description": self.weather_description,
            "icon": self.icon,
            "timezone": self.timezone,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class SavedLocation(BaseModel):
    """Saved locations model for user's favorite cities."""
    __tablename__ = "saved_locations"
    
    city = Column(String(100), nullable=False)
    country = Column(String(50), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    nickname = Column(String(100), nullable=True)
    
    def to_dict(self):
        """Convert saved location to dictionary."""
        return {
            "id": self.id,
            "city": self.city,
            "country": self.country,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "nickname": self.nickname,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }