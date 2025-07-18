"""UI components for Todo App."""

import reflex as rx
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../packages"))
from shared.components import themed_button, themed_input, themed_card, error_message, success_message
from shared.theme import DARK_THEME
from .state import TodoState

def todo_form() -> rx.Component:
    """Component for adding new todos."""
    return themed_card(
        rx.heading(
            "Add New Todo",
            size="lg",
            color=DARK_THEME["text_primary"],
            margin_bottom="1rem",
        ),
        rx.vstack(
            themed_input(
                placeholder="Todo title...",
                value=TodoState.new_todo_title,
                on_change=TodoState.set_new_todo_title,
            ),
            themed_input(
                placeholder="Description (optional)...",
                value=TodoState.new_todo_description,
                on_change=TodoState.set_new_todo_description,
            ),
            rx.select(
                ["low", "medium", "high"],
                value=TodoState.new_todo_priority,
                on_change=TodoState.set_new_todo_priority,
                style={
                    "background_color": DARK_THEME["surface_variant"],
                    "border": f"1px solid {DARK_THEME['border_light']}",
                    "border_radius": "8px",
                    "padding": "0.75rem 1rem",
                    "color": DARK_THEME["text_primary"],
                    "width": "100%",
                }
            ),
            themed_button(
                "Add Todo",
                on_click=TodoState.add_todo,
                variant="primary",
                width="100%",
                disabled=TodoState.is_loading,
            ),
            spacing="1rem",
            width="100%",
        ),
        width="100%",
        margin_bottom="2rem",
    )

def todo_filters() -> rx.Component:
    """Component for filtering todos."""
    return themed_card(
        rx.heading(
            "Filters",
            size="md",
            color=DARK_THEME["text_primary"],
            margin_bottom="1rem",
        ),
        rx.hstack(
            rx.vstack(
                rx.text(
                    "Status",
                    color=DARK_THEME["text_secondary"],
                    font_weight="500",
                    margin_bottom="0.5rem",
                ),
                rx.select(
                    ["all", "pending", "completed"],
                    value=TodoState.filter_status,
                    on_change=TodoState.set_filter_status,
                    style={
                        "background_color": DARK_THEME["surface_variant"],
                        "border": f"1px solid {DARK_THEME['border_light']}",
                        "border_radius": "8px",
                        "padding": "0.5rem",
                        "color": DARK_THEME["text_primary"],
                        "width": "100%",
                    }
                ),
                spacing="0.5rem",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Priority",
                    color=DARK_THEME["text_secondary"],
                    font_weight="500",
                    margin_bottom="0.5rem",
                ),
                rx.select(
                    ["all", "low", "medium", "high"],
                    value=TodoState.filter_priority,
                    on_change=TodoState.set_filter_priority,
                    style={
                        "background_color": DARK_THEME["surface_variant"],
                        "border": f"1px solid {DARK_THEME['border_light']}",
                        "border_radius": "8px",
                        "padding": "0.5rem",
                        "color": DARK_THEME["text_primary"],
                        "width": "100%",
                    }
                ),
                spacing="0.5rem",
                width="100%",
            ),
            spacing="2rem",
            width="100%",
        ),
        width="100%",
        margin_bottom="2rem",
    )

def todo_stats() -> rx.Component:
    """Component for displaying todo statistics."""
    return themed_card(
        rx.heading(
            "Statistics",
            size="md",
            color=DARK_THEME["text_primary"],
            margin_bottom="1rem",
        ),
        rx.hstack(
            rx.vstack(
                rx.text(
                    TodoState.todos_count["total"],
                    font_size="2xl",
                    font_weight="bold",
                    color=DARK_THEME["primary"],
                ),
                rx.text(
                    "Total",
                    color=DARK_THEME["text_secondary"],
                    font_size="sm",
                ),
                align="center",
                spacing="0.25rem",
            ),
            rx.vstack(
                rx.text(
                    TodoState.todos_count["pending"],
                    font_size="2xl",
                    font_weight="bold",
                    color=DARK_THEME["warning"],
                ),
                rx.text(
                    "Pending",
                    color=DARK_THEME["text_secondary"],
                    font_size="sm",
                ),
                align="center",
                spacing="0.25rem",
            ),
            rx.vstack(
                rx.text(
                    TodoState.todos_count["completed"],
                    font_size="2xl",
                    font_weight="bold",
                    color=DARK_THEME["success"],
                ),
                rx.text(
                    "Completed",
                    color=DARK_THEME["text_secondary"],
                    font_size="sm",
                ),
                align="center",
                spacing="0.25rem",
            ),
            justify="space-around",
            width="100%",
        ),
        width="100%",
        margin_bottom="2rem",
    )

def todo_item(todo: dict) -> rx.Component:
    """Component for individual todo item."""
    priority_colors = {
        "low": DARK_THEME["text_muted"],
        "medium": DARK_THEME["warning"],
        "high": DARK_THEME["error"],
    }
    
    return themed_card(
        rx.hstack(
            rx.checkbox(
                is_checked=todo["completed"],
                on_change=lambda: TodoState.toggle_todo(todo["id"]),
                style={
                    "color": DARK_THEME["primary"],
                    "scale": "1.2",
                }
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        todo["title"],
                        font_weight="600",
                        color=DARK_THEME["text_primary"],
                        text_decoration="line-through" if todo["completed"] else "none",
                        opacity="0.6" if todo["completed"] else "1",
                    ),
                    rx.badge(
                        todo["priority"],
                        style={
                            "background_color": f"{priority_colors[todo['priority']]}20",
                            "color": priority_colors[todo["priority"]],
                            "border": f"1px solid {priority_colors[todo['priority']]}30",
                            "border_radius": "12px",
                            "padding": "0.25rem 0.5rem",
                            "font_size": "xs",
                            "font_weight": "500",
                        }
                    ),
                    justify="space-between",
                    align="center",
                    width="100%",
                ),
                rx.cond(
                    todo["description"],
                    rx.text(
                        todo["description"],
                        color=DARK_THEME["text_secondary"],
                        font_size="sm",
                        opacity="0.6" if todo["completed"] else "1",
                    ),
                ),
                align="start",
                spacing="0.5rem",
                width="100%",
            ),
            themed_button(
                "Delete",
                on_click=lambda: TodoState.delete_todo(todo["id"]),
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
            justify="space-between",
            align="start",
            width="100%",
        ),
        margin_bottom="1rem",
        opacity="0.7" if todo["completed"] else "1",
    )

def todo_list() -> rx.Component:
    """Component for displaying list of todos."""
    return rx.box(
        rx.cond(
            TodoState.filtered_todos,
            rx.vstack(
                rx.foreach(
                    TodoState.filtered_todos,
                    todo_item,
                ),
                spacing="0",
                width="100%",
            ),
            rx.box(
                rx.text(
                    "No todos found",
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
        ),
        width="100%",
    )