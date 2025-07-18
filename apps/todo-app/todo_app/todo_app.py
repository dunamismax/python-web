"""Main Todo App application."""

import reflex as rx
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../packages"))
from shared.components import page_header, navigation_bar, error_message, success_message
from shared.theme import get_base_style, DARK_THEME
from .state import TodoState
from .components import todo_form, todo_filters, todo_stats, todo_list

def index() -> rx.Component:
    """Main page of the Todo App."""
    return rx.box(
        navigation_bar("Todo App"),
        rx.container(
            page_header(
                "Task Manager",
                "Organize your tasks efficiently with our beautiful todo app"
            ),
            
            rx.cond(
                TodoState.error_message,
                error_message(TodoState.error_message),
            ),
            
            rx.cond(
                TodoState.success_message,
                success_message(TodoState.success_message),
            ),
            
            rx.grid(
                rx.grid_item(
                    rx.vstack(
                        todo_form(),
                        todo_filters(),
                        todo_stats(),
                        spacing="0",
                        width="100%",
                    ),
                    col_span=1,
                ),
                rx.grid_item(
                    todo_list(),
                    col_span=2,
                ),
                template_columns="1fr 2fr",
                gap="2rem",
                width="100%",
            ),
            
            max_width="1200px",
            padding="0 2rem",
        ),
        style=get_base_style(),
        min_height="100vh",
        on_click=TodoState.clear_messages,
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