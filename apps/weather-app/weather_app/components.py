"""UI components for Weather App."""

import reflex as rx
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../packages"))
from shared.components import themed_button, themed_input, themed_card, error_message, success_message, loading_spinner
from shared.theme import DARK_THEME
from .state import WeatherState

def weather_search() -> rx.Component:
    """Component for searching weather."""
    return themed_card(
        rx.heading(
            "Weather Search",
            size="lg",
            color=DARK_THEME["text_primary"],
            margin_bottom="1rem",
        ),
        rx.vstack(
            rx.hstack(
                themed_input(
                    placeholder="Enter city name...",
                    value=WeatherState.search_city,
                    on_change=WeatherState.set_search_city,
                ),
                themed_button(
                    "Search",
                    on_click=WeatherState.search_weather,
                    variant="primary",
                    disabled=WeatherState.is_loading,
                ),
                spacing="1rem",
                width="100%",
            ),
            rx.cond(
                WeatherState.is_loading,
                rx.hstack(
                    loading_spinner("sm"),
                    rx.text(
                        "Fetching weather data...",
                        color=DARK_THEME["text_secondary"],
                    ),
                    spacing="0.5rem",
                    align="center",
                )
            ),
            spacing="1rem",
            width="100%",
        ),
        width="100%",
        margin_bottom="2rem",
    )

def weather_navigation() -> rx.Component:
    """Component for weather app navigation."""
    return themed_card(
        rx.hstack(
            themed_button(
                "Current",
                on_click=lambda: WeatherState.set_current_view("current"),
                variant="primary" if WeatherState.current_view == "current" else "outline",
            ),
            themed_button(
                "Forecast",
                on_click=WeatherState.get_forecast,
                variant="primary" if WeatherState.current_view == "forecast" else "outline",
                disabled=~WeatherState.has_current_weather,
            ),
            themed_button(
                "History",
                on_click=lambda: WeatherState.set_current_view("history"),
                variant="primary" if WeatherState.current_view == "history" else "outline",
            ),
            themed_button(
                "Saved",
                on_click=lambda: WeatherState.set_current_view("locations"),
                variant="primary" if WeatherState.current_view == "locations" else "outline",
            ),
            spacing="1rem",
            justify="center",
            width="100%",
        ),
        width="100%",
        margin_bottom="2rem",
    )

def current_weather_display() -> rx.Component:
    """Component for displaying current weather."""
    return rx.cond(
        WeatherState.has_current_weather,
        themed_card(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            rx.text(WeatherState.current_weather["city"]),
                            size="xl",
                            color=DARK_THEME["text_primary"],
                        ),
                        rx.text(
                            rx.text(WeatherState.current_weather["country"]),
                            color=DARK_THEME["text_secondary"],
                            font_size="lg",
                        ),
                        align="start",
                        spacing="0.25rem",
                    ),
                    themed_button(
                        "Save Location",
                        on_click=WeatherState.save_current_location,
                        variant="secondary",
                        size="sm",
                    ),
                    justify="space-between",
                    align="start",
                    width="100%",
                ),
                
                rx.hstack(
                    rx.image(
                        src=WeatherState.weather_icon_url,
                        alt="Weather icon",
                        width="80px",
                        height="80px",
                    ),
                    rx.vstack(
                        rx.text(
                            f"{WeatherState.current_weather['temperature']}°C",
                            font_size="3xl",
                            font_weight="bold",
                            color=DARK_THEME["text_primary"],
                        ),
                        rx.text(
                            f"Feels like {WeatherState.current_weather['feels_like']}°C",
                            color=DARK_THEME["text_secondary"],
                        ),
                        align="start",
                        spacing="0.25rem",
                    ),
                    rx.vstack(
                        rx.text(
                            rx.text(WeatherState.current_weather["weather_description"]),
                            font_weight="600",
                            color=DARK_THEME["text_primary"],
                        ),
                        rx.text(
                            rx.text(WeatherState.current_weather["weather_main"]),
                            color=DARK_THEME["text_secondary"],
                            font_size="sm",
                        ),
                        align="start",
                        spacing="0.25rem",
                    ),
                    spacing="2rem",
                    align="center",
                    width="100%",
                ),
                
                rx.grid(
                    rx.box(
                        rx.text(
                            "Humidity",
                            color=DARK_THEME["text_secondary"],
                            font_size="sm",
                        ),
                        rx.text(
                            f"{WeatherState.current_weather['humidity']}%",
                            font_weight="600",
                            color=DARK_THEME["text_primary"],
                            font_size="lg",
                        ),
                    ),
                    rx.box(
                        rx.text(
                            "Pressure",
                            color=DARK_THEME["text_secondary"],
                            font_size="sm",
                        ),
                        rx.text(
                            f"{WeatherState.current_weather['pressure']} hPa",
                            font_weight="600",
                            color=DARK_THEME["text_primary"],
                            font_size="lg",
                        ),
                    ),
                    rx.box(
                        rx.text(
                            "Wind Speed",
                            color=DARK_THEME["text_secondary"],
                            font_size="sm",
                        ),
                        rx.text(
                            f"{WeatherState.current_weather['wind_speed']} m/s",
                            font_weight="600",
                            color=DARK_THEME["text_primary"],
                            font_size="lg",
                        ),
                    ),
                    rx.box(
                        rx.text(
                            "Wind Direction",
                            color=DARK_THEME["text_secondary"],
                            font_size="sm",
                        ),
                        rx.text(
                            WeatherState.wind_direction_name,
                            font_weight="600",
                            color=DARK_THEME["text_primary"],
                            font_size="lg",
                        ),
                    ),
                    template_columns="repeat(2, 1fr)",
                    gap="2rem",
                    width="100%",
                    margin_top="2rem",
                ),
                
                spacing="2rem",
                width="100%",
            ),
            width="100%",
        ),
        rx.box(
            rx.text(
                "Search for a city to see weather data",
                color=DARK_THEME["text_muted"],
                font_size="lg",
                text_align="center",
            ),
            style={
                "background_color": DARK_THEME["surface"],
                "border": f"2px dashed {DARK_THEME['border']}",
                "border_radius": "12px",
                "padding": "3rem",
                "text_align": "center",
            }
        )
    )

def forecast_display() -> rx.Component:
    """Component for displaying weather forecast."""
    return rx.cond(
        WeatherState.forecast_data,
        rx.vstack(
            rx.heading(
                "5-Day Forecast",
                size="lg",
                color=DARK_THEME["text_primary"],
                margin_bottom="1rem",
            ),
            rx.vstack(
                rx.foreach(
                    WeatherState.forecast_data,
                    lambda item: themed_card(
                        rx.hstack(
                            rx.text(
                                item["date"],
                                font_weight="600",
                                color=DARK_THEME["text_primary"],
                            ),
                            rx.image(
                                src=f"https://openweathermap.org/img/wn/{item['icon']}@2x.png",
                                alt="Weather icon",
                                width="40px",
                                height="40px",
                            ),
                            rx.text(
                                f"{item['temperature']}°C",
                                font_weight="600",
                                color=DARK_THEME["primary"],
                            ),
                            rx.text(
                                item["weather_description"],
                                color=DARK_THEME["text_secondary"],
                            ),
                            rx.text(
                                f"Wind: {item['wind_speed']} m/s",
                                color=DARK_THEME["text_muted"],
                                font_size="sm",
                            ),
                            justify="space-between",
                            align="center",
                            width="100%",
                        ),
                        margin_bottom="0.5rem",
                    )
                ),
                spacing="0",
                width="100%",
            ),
            spacing="0",
            width="100%",
        ),
        rx.box(
            rx.text(
                "No forecast data available",
                color=DARK_THEME["text_muted"],
                font_size="lg",
                text_align="center",
            ),
            style={
                "background_color": DARK_THEME["surface"],
                "border": f"2px dashed {DARK_THEME['border']}",
                "border_radius": "12px",
                "padding": "3rem",
                "text_align": "center",
            }
        )
    )

def weather_history() -> rx.Component:
    """Component for displaying weather history."""
    return rx.cond(
        WeatherState.weather_history,
        rx.vstack(
            rx.heading(
                "Recent Searches",
                size="lg",
                color=DARK_THEME["text_primary"],
                margin_bottom="1rem",
            ),
            rx.vstack(
                rx.foreach(
                    WeatherState.weather_history,
                    lambda item: themed_card(
                        rx.hstack(
                            rx.vstack(
                                rx.text(
                                    f"{item['city']}, {item['country']}",
                                    font_weight="600",
                                    color=DARK_THEME["text_primary"],
                                ),
                                rx.text(
                                    item["created_at"][:16],  # Date and time
                                    color=DARK_THEME["text_muted"],
                                    font_size="sm",
                                ),
                                align="start",
                                spacing="0.25rem",
                            ),
                            rx.text(
                                f"{item['temperature']}°C",
                                font_weight="600",
                                color=DARK_THEME["primary"],
                                font_size="lg",
                            ),
                            rx.text(
                                item["weather_description"],
                                color=DARK_THEME["text_secondary"],
                            ),
                            themed_button(
                                "View",
                                on_click=lambda city=item["city"]: WeatherState.load_weather_for_location(city),
                                variant="outline",
                                size="sm",
                            ),
                            justify="space-between",
                            align="center",
                            width="100%",
                        ),
                        margin_bottom="0.5rem",
                    )
                ),
                spacing="0",
                width="100%",
            ),
            spacing="0",
            width="100%",
        ),
        rx.box(
            rx.text(
                "No search history available",
                color=DARK_THEME["text_muted"],
                font_size="lg",
                text_align="center",
            ),
            style={
                "background_color": DARK_THEME["surface"],
                "border": f"2px dashed {DARK_THEME['border']}",
                "border_radius": "12px",
                "padding": "3rem",
                "text_align": "center",
            }
        )
    )

def saved_locations() -> rx.Component:
    """Component for displaying saved locations."""
    return rx.cond(
        WeatherState.saved_locations,
        rx.vstack(
            rx.heading(
                "Saved Locations",
                size="lg",
                color=DARK_THEME["text_primary"],
                margin_bottom="1rem",
            ),
            rx.vstack(
                rx.foreach(
                    WeatherState.saved_locations,
                    lambda item: themed_card(
                        rx.hstack(
                            rx.vstack(
                                rx.text(
                                    f"{item['city']}, {item['country']}",
                                    font_weight="600",
                                    color=DARK_THEME["text_primary"],
                                ),
                                rx.text(
                                    f"Lat: {item['latitude']:.2f}, Lon: {item['longitude']:.2f}",
                                    color=DARK_THEME["text_muted"],
                                    font_size="sm",
                                ),
                                align="start",
                                spacing="0.25rem",
                            ),
                            rx.hstack(
                                themed_button(
                                    "Load Weather",
                                    on_click=lambda city=item["city"]: WeatherState.load_weather_for_location(city),
                                    variant="primary",
                                    size="sm",
                                ),
                                themed_button(
                                    "Delete",
                                    on_click=lambda id=item["id"]: WeatherState.delete_saved_location(id),
                                    variant="outline",
                                    size="sm",
                                    style={
                                        "color": DARK_THEME["error"],
                                        "border_color": DARK_THEME["error"],
                                        "_hover": {
                                            "background_color": f"{DARK_THEME['error']}10",
                                        }
                                    }
                                ),
                                spacing="0.5rem",
                            ),
                            justify="space-between",
                            align="center",
                            width="100%",
                        ),
                        margin_bottom="0.5rem",
                    )
                ),
                spacing="0",
                width="100%",
            ),
            spacing="0",
            width="100%",
        ),
        rx.box(
            rx.text(
                "No saved locations",
                color=DARK_THEME["text_muted"],
                font_size="lg",
                text_align="center",
            ),
            style={
                "background_color": DARK_THEME["surface"],
                "border": f"2px dashed {DARK_THEME['border']}",
                "border_radius": "12px",
                "padding": "3rem",
                "text_align": "center",
            }
        )
    )