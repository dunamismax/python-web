#!/bin/bash

# Deployment script for Python Web apps

set -e

APP_NAME=$1
ENVIRONMENT=${2:-production}

if [ -z "$APP_NAME" ]; then
    echo "Usage: $0 <app-name> [environment]"
    echo "Available apps: todo, weather"
    exit 1
fi

if [ "$APP_NAME" != "todo" ] && [ "$APP_NAME" != "weather" ]; then
    echo "Invalid app name. Available apps: todo, weather"
    exit 1
fi

echo "Deploying $APP_NAME app to $ENVIRONMENT environment..."

# Set app directory
if [ "$APP_NAME" = "todo" ]; then
    APP_DIR="apps/todo-app"
elif [ "$APP_NAME" = "weather" ]; then
    APP_DIR="apps/weather-app"
fi

# Build the app
echo "Building $APP_NAME app..."
cd $APP_DIR
reflex export

# Create deployment package
echo "Creating deployment package..."
mkdir -p ../../dist/$APP_NAME
cp -r .web/export/* ../../dist/$APP_NAME/
cp requirements.txt ../../dist/$APP_NAME/

# Copy environment configuration
if [ -f ".env.$ENVIRONMENT" ]; then
    cp .env.$ENVIRONMENT ../../dist/$APP_NAME/.env
fi

cd ../..

echo "Deployment package created in dist/$APP_NAME"
echo "Deploy this directory to your hosting platform"

# Example commands for different platforms:
echo ""
echo "Example deployment commands:"
echo "  Docker: docker build -t $APP_NAME-app dist/$APP_NAME"
echo "  Heroku: cd dist/$APP_NAME && git init && heroku create && git push heroku main"
echo "  Vercel: cd dist/$APP_NAME && vercel deploy"