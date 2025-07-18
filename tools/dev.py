#!/usr/bin/env python3
"""Development tools and scripts for the Python Web monorepo."""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def run_command(command: str, cwd: str = None) -> int:
    """Run a shell command and return exit code."""
    print(f"Running: {command}")
    if cwd:
        print(f"In directory: {cwd}")
    
    result = subprocess.run(command, shell=True, cwd=cwd)
    return result.returncode

def install_dependencies():
    """Install dependencies for all apps."""
    print("Installing dependencies for all apps...")
    
    # Install root dependencies
    if run_command("pip install -e .") != 0:
        print("Failed to install root dependencies")
        return False
    
    # Install todo app dependencies
    todo_path = "apps/todo-app"
    if run_command("pip install -r requirements.txt", cwd=todo_path) != 0:
        print("Failed to install todo app dependencies")
        return False
    
    # Install weather app dependencies
    weather_path = "apps/weather-app"
    if run_command("pip install -r requirements.txt", cwd=weather_path) != 0:
        print("Failed to install weather app dependencies")
        return False
    
    print("All dependencies installed successfully!")
    return True

def run_todo_app():
    """Run the todo app in development mode."""
    print("Starting Todo App...")
    todo_path = "apps/todo-app"
    os.chdir(todo_path)
    return run_command("reflex run")

def run_weather_app():
    """Run the weather app in development mode."""
    print("Starting Weather App...")
    weather_path = "apps/weather-app"
    os.chdir(weather_path)
    return run_command("reflex run")

def build_todo_app():
    """Build the todo app for production."""
    print("Building Todo App...")
    todo_path = "apps/todo-app"
    return run_command("reflex export", cwd=todo_path)

def build_weather_app():
    """Build the weather app for production."""
    print("Building Weather App...")
    weather_path = "apps/weather-app"
    return run_command("reflex export", cwd=weather_path)

def format_code():
    """Format code using black and isort."""
    print("Formatting code...")
    
    # Format with black
    if run_command("black .") != 0:
        print("Black formatting failed")
        return False
    
    # Sort imports with isort
    if run_command("isort .") != 0:
        print("isort failed")
        return False
    
    print("Code formatting completed!")
    return True

def lint_code():
    """Lint code using flake8."""
    print("Linting code...")
    return run_command("flake8 .") == 0

def type_check():
    """Type check code using mypy."""
    print("Type checking...")
    return run_command("mypy .") == 0

def run_tests():
    """Run tests for all apps."""
    print("Running tests...")
    return run_command("pytest") == 0

def clean():
    """Clean build artifacts and cache files."""
    print("Cleaning build artifacts...")
    
    # Remove Python cache
    run_command("find . -type d -name __pycache__ -exec rm -rf {} +")
    run_command("find . -type f -name '*.pyc' -delete")
    
    # Remove build directories
    run_command("rm -rf build/")
    run_command("rm -rf dist/")
    run_command("rm -rf *.egg-info/")
    
    # Remove Reflex build artifacts
    run_command("rm -rf apps/todo-app/.web/")
    run_command("rm -rf apps/weather-app/.web/")
    
    print("Cleanup completed!")

def init_reflex_apps():
    """Initialize Reflex apps if needed."""
    print("Initializing Reflex apps...")
    
    # Initialize todo app
    todo_path = "apps/todo-app"
    if not os.path.exists(os.path.join(todo_path, ".web")):
        print("Initializing Todo App...")
        run_command("reflex init", cwd=todo_path)
    
    # Initialize weather app
    weather_path = "apps/weather-app"
    if not os.path.exists(os.path.join(weather_path, ".web")):
        print("Initializing Weather App...")
        run_command("reflex init", cwd=weather_path)
    
    print("Reflex apps initialized!")

def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(description="Python Web Development Tools")
    parser.add_argument("command", choices=[
        "install", "todo", "weather", "build-todo", "build-weather",
        "format", "lint", "typecheck", "test", "clean", "init"
    ], help="Command to run")
    
    args = parser.parse_args()
    
    # Ensure we're in the project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    if args.command == "install":
        install_dependencies()
    elif args.command == "todo":
        init_reflex_apps()
        run_todo_app()
    elif args.command == "weather":
        init_reflex_apps()
        run_weather_app()
    elif args.command == "build-todo":
        build_todo_app()
    elif args.command == "build-weather":
        build_weather_app()
    elif args.command == "format":
        format_code()
    elif args.command == "lint":
        lint_code()
    elif args.command == "typecheck":
        type_check()
    elif args.command == "test":
        run_tests()
    elif args.command == "clean":
        clean()
    elif args.command == "init":
        init_reflex_apps()

if __name__ == "__main__":
    main()