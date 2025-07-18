"""Main Weather App application."""

import reflex as rx
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../packages"))
from shared.components import page_header, navigation_bar, error_message, success_message
from shared.theme import get_base_style, DARK_THEME
from .state import WeatherState
from .components import (
    weather_search,
    weather_navigation,
    current_weather_display,
    forecast_display,
    weather_history,
    saved_locations
)

def index() -> rx.Component:
    """Main page of the Weather App."""
    return rx.box(
        navigation_bar("Weather App"),
        rx.container(
            page_header(
                "Weather Dashboard",
                "Get current weather, forecasts, and save your favorite locations"
            ),
            
            rx.cond(
                WeatherState.error_message,
                error_message(WeatherState.error_message),
            ),
            
            rx.cond(
                WeatherState.success_message,
                success_message(WeatherState.success_message),
            ),
            
            weather_search(),
            weather_navigation(),
            
            rx.cond(
                WeatherState.current_view == "current",
                current_weather_display(),
                rx.cond(
                    WeatherState.current_view == "forecast",
                    forecast_display(),
                    rx.cond(
                        WeatherState.current_view == "history",
                        weather_history(),
                        saved_locations()
                    )
                )
            ),
            
            max_width="1000px",
            padding="0 2rem",
        ),
        style=get_base_style(),
        min_height="100vh",
        on_click=WeatherState.clear_messages,
    )

app = rx.App(
    style={
        "font_family": "Inter, system-ui, sans-serif",
        "background_color": DARK_THEME["background"],
    }
)

app.add_page(index, route="/")

if __name__ == "__main__":
    app.run()