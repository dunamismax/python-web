"""Reflex configuration for Weather App."""

import reflex as rx

config = rx.Config(
    app_name="weather_app",
    frontend_port=3001,
    backend_port=8001,
    api_url="http://localhost:8001",
    deploy_url="http://localhost:3001",
    env=rx.Env.DEV,
)