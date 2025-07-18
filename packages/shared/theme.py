"""Shared dark theme configuration for all apps."""

import reflex as rx

DARK_THEME = {
    "background": "#0a0a0a",
    "surface": "#1a1a1a",
    "surface_variant": "#2a2a2a",
    "primary": "#3b82f6",
    "primary_variant": "#1d4ed8",
    "secondary": "#10b981",
    "secondary_variant": "#059669",
    "accent": "#8b5cf6",
    "error": "#ef4444",
    "warning": "#f59e0b",
    "success": "#10b981",
    "text_primary": "#ffffff",
    "text_secondary": "#a1a1aa",
    "text_muted": "#71717a",
    "border": "#27272a",
    "border_light": "#3f3f46",
}

def get_base_style() -> dict:
    """Get base styles for dark theme."""
    return {
        "background_color": DARK_THEME["background"],
        "color": DARK_THEME["text_primary"],
        "font_family": "Inter, system-ui, sans-serif",
    }

def get_container_style() -> dict:
    """Get container styles for dark theme."""
    return {
        "background_color": DARK_THEME["surface"],
        "border_radius": "12px",
        "border": f"1px solid {DARK_THEME['border']}",
        "padding": "1.5rem",
        "box_shadow": "0 4px 6px -1px rgb(0 0 0 / 0.1)",
    }

def get_button_style(variant: str = "primary") -> dict:
    """Get button styles for dark theme."""
    base_style = {
        "border_radius": "8px",
        "padding": "0.75rem 1.5rem",
        "font_weight": "500",
        "transition": "all 0.2s ease",
        "border": "none",
        "cursor": "pointer",
        "_hover": {
            "transform": "translateY(-1px)",
        }
    }
    
    if variant == "primary":
        base_style.update({
            "background_color": DARK_THEME["primary"],
            "color": "white",
            "_hover": {
                **base_style["_hover"],
                "background_color": DARK_THEME["primary_variant"],
            }
        })
    elif variant == "secondary":
        base_style.update({
            "background_color": DARK_THEME["secondary"],
            "color": "white",
            "_hover": {
                **base_style["_hover"],
                "background_color": DARK_THEME["secondary_variant"],
            }
        })
    elif variant == "outline":
        base_style.update({
            "background_color": "transparent",
            "color": DARK_THEME["text_primary"],
            "border": f"1px solid {DARK_THEME['border_light']}",
            "_hover": {
                **base_style["_hover"],
                "background_color": DARK_THEME["surface_variant"],
            }
        })
    
    return base_style

def get_input_style() -> dict:
    """Get input styles for dark theme."""
    return {
        "background_color": DARK_THEME["surface_variant"],
        "border": f"1px solid {DARK_THEME['border_light']}",
        "border_radius": "8px",
        "padding": "0.75rem 1rem",
        "color": DARK_THEME["text_primary"],
        "_placeholder": {
            "color": DARK_THEME["text_muted"],
        },
        "_focus": {
            "border_color": DARK_THEME["primary"],
            "outline": "none",
            "box_shadow": f"0 0 0 3px {DARK_THEME['primary']}20",
        }
    }

def get_card_style() -> dict:
    """Get card styles for dark theme."""
    return {
        "background_color": DARK_THEME["surface"],
        "border": f"1px solid {DARK_THEME['border']}",
        "border_radius": "12px",
        "padding": "1.5rem",
        "box_shadow": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -1px rgb(0 0 0 / 0.06)",
        "_hover": {
            "box_shadow": "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -2px rgb(0 0 0 / 0.05)",
            "transform": "translateY(-2px)",
            "transition": "all 0.2s ease",
        }
    }