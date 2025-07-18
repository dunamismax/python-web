"""Reflex configuration for Todo App."""

import reflex as rx

config = rx.Config(
    app_name="todo_app",
    frontend_port=3000,
    backend_port=8000,
    api_url="http://localhost:8000",
    deploy_url="http://localhost:3000",
    env=rx.Env.DEV,
)