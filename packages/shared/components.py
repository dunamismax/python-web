"""Shared UI components for all apps."""

import reflex as rx
from .theme import get_button_style, get_input_style, get_card_style, DARK_THEME

def themed_button(text: str, on_click=None, variant: str = "primary", **kwargs) -> rx.Component:
    """Create a themed button component."""
    return rx.button(
        text,
        on_click=on_click,
        style=get_button_style(variant),
        **kwargs
    )

def themed_input(placeholder: str = "", value="", on_change=None, **kwargs) -> rx.Component:
    """Create a themed input component."""
    return rx.input(
        placeholder=placeholder,
        value=value,
        on_change=on_change,
        style=get_input_style(),
        **kwargs
    )

def themed_card(*children, **kwargs) -> rx.Component:
    """Create a themed card component."""
    return rx.box(
        *children,
        style=get_card_style(),
        **kwargs
    )

def loading_spinner(size: str = "md") -> rx.Component:
    """Create a loading spinner component."""
    size_map = {
        "sm": "1rem",
        "md": "1.5rem",
        "lg": "2rem",
        "xl": "3rem"
    }
    
    return rx.box(
        style={
            "width": size_map[size],
            "height": size_map[size],
            "border": f"2px solid {DARK_THEME['border']}",
            "border_top": f"2px solid {DARK_THEME['primary']}",
            "border_radius": "50%",
            "animation": "spin 1s linear infinite",
        }
    )

def error_message(message: str) -> rx.Component:
    """Create an error message component."""
    return rx.box(
        rx.text(
            message,
            color=DARK_THEME["error"],
            font_weight="500",
        ),
        style={
            "background_color": f"{DARK_THEME['error']}10",
            "border": f"1px solid {DARK_THEME['error']}30",
            "border_radius": "8px",
            "padding": "0.75rem 1rem",
            "margin": "0.5rem 0",
        }
    )

def success_message(message: str) -> rx.Component:
    """Create a success message component."""
    return rx.box(
        rx.text(
            message,
            color=DARK_THEME["success"],
            font_weight="500",
        ),
        style={
            "background_color": f"{DARK_THEME['success']}10",
            "border": f"1px solid {DARK_THEME['success']}30",
            "border_radius": "8px",
            "padding": "0.75rem 1rem",
            "margin": "0.5rem 0",
        }
    )

def page_header(title: str, subtitle: str = "") -> rx.Component:
    """Create a page header component."""
    components = [
        rx.heading(
            title,
            size="2xl",
            color=DARK_THEME["text_primary"],
            font_weight="700",
            margin_bottom="0.5rem",
        )
    ]
    
    if subtitle:
        components.append(
            rx.text(
                subtitle,
                color=DARK_THEME["text_secondary"],
                font_size="lg",
                margin_bottom="2rem",
            )
        )
    
    return rx.box(
        *components,
        margin_bottom="2rem",
    )

def navigation_bar(app_name: str, links: list = None) -> rx.Component:
    """Create a navigation bar component."""
    nav_items = [
        rx.heading(
            app_name,
            size="lg",
            color=DARK_THEME["text_primary"],
            font_weight="600",
        )
    ]
    
    if links:
        nav_links = []
        for link in links:
            nav_links.append(
                rx.link(
                    link["text"],
                    href=link["href"],
                    style={
                        "color": DARK_THEME["text_secondary"],
                        "text_decoration": "none",
                        "padding": "0.5rem 1rem",
                        "border_radius": "6px",
                        "_hover": {
                            "color": DARK_THEME["text_primary"],
                            "background_color": DARK_THEME["surface_variant"],
                        }
                    }
                )
            )
        
        nav_items.append(
            rx.hstack(
                *nav_links,
                spacing="1rem",
            )
        )
    
    return rx.box(
        rx.hstack(
            *nav_items,
            justify="space-between",
            align="center",
            width="100%",
        ),
        style={
            "background_color": DARK_THEME["surface"],
            "border_bottom": f"1px solid {DARK_THEME['border']}",
            "padding": "1rem 2rem",
            "margin_bottom": "2rem",
        }
    )