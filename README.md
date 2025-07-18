# Python Web Monorepo

A complete Python-based web development monorepo featuring modern applications built with Reflex, FastAPI, and SQLite. This repository contains two fully-featured demo applications with beautiful dark themes and comprehensive tooling for development and deployment.

## 🚀 Features

- **Full-Stack Python**: Build entire web applications using only Python
- **Modern Dark Theme**: Beautiful, consistent UI across all applications
- **Monorepo Structure**: Organized codebase with shared components and utilities
- **Database Integration**: SQLAlchemy ORM with SQLite for data persistence
- **API Integration**: RESTful APIs and external service integration
- **Development Tools**: Comprehensive tooling for development, testing, and deployment

## 📱 Applications

### Todo App
A feature-rich task management application with:
- ✅ Create, update, and delete todos
- 🏷️ Priority levels (low, medium, high)
- 🔍 Filter by status and priority
- 📊 Statistics dashboard
- 💾 Persistent SQLite storage

**Ports**: Frontend: 3000, Backend: 8000

### Weather App
A beautiful weather dashboard with:
- 🌤️ Current weather conditions
- 📅 5-day weather forecast
- 📍 Save favorite locations
- 📋 Search history
- 🌐 OpenWeatherMap API integration

**Ports**: Frontend: 3001, Backend: 8001

## 🛠️ Tech Stack

- **Frontend Framework**: [Reflex](https://reflex.dev/) - Full-stack Python framework
- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) - High-performance API framework
- **Database**: [SQLite](https://www.sqlite.org/) with [SQLAlchemy](https://www.sqlalchemy.org/) ORM
- **Development Environment**: Reflex CLI for build and development
- **Code Quality**: Black, isort, flake8, mypy for formatting and linting

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+ (for Reflex frontend compilation)
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dunamismax/python-web.git
   cd python-web
   ```

2. **Install dependencies**:
   ```bash
   make install
   # or
   python tools/dev.py install
   ```

3. **Initialize applications**:
   ```bash
   make init
   # or
   python tools/dev.py init
   ```

4. **Set up Weather App API key** (optional):
   ```bash
   cd apps/weather-app
   cp .env.example .env
   # Edit .env and add your OpenWeatherMap API key
   ```

### Running Applications

**Todo App**:
```bash
make todo
# or
python tools/dev.py todo
```
Open http://localhost:3000

**Weather App**:
```bash
make weather
# or
python tools/dev.py weather
```
Open http://localhost:3001

## 📁 Project Structure

```
python-web/
├── apps/
│   ├── todo-app/           # Todo application
│   │   ├── todo_app/       # App source code
│   │   ├── tests/          # App tests
│   │   ├── requirements.txt
│   │   ├── rxconfig.py     # Reflex configuration
│   │   └── Dockerfile
│   └── weather-app/        # Weather application
│       ├── weather_app/    # App source code
│       ├── tests/          # App tests
│       ├── requirements.txt
│       ├── rxconfig.py     # Reflex configuration
│       ├── .env.example    # Environment template
│       └── Dockerfile
├── packages/
│   └── shared/             # Shared components and utilities
│       ├── __init__.py
│       ├── theme.py        # Dark theme configuration
│       ├── components.py   # Reusable UI components
│       └── database.py     # Database utilities
├── tools/
│   └── dev.py             # Development CLI tool
├── scripts/
│   └── deploy.sh          # Deployment script
├── docs/                  # Documentation
├── data/                  # SQLite databases (auto-created)
├── pyproject.toml         # Project configuration
├── Makefile              # Development commands
├── docker-compose.yml    # Container orchestration
└── README.md
```

## 🧰 Development Commands

All commands can be run using either `make` or the Python development tool:

| Command | Make | Python Tool | Description |
|---------|------|-------------|-------------|
| Install dependencies | `make install` | `python tools/dev.py install` | Install all project dependencies |
| Initialize apps | `make init` | `python tools/dev.py init` | Initialize Reflex applications |
| Run Todo app | `make todo` | `python tools/dev.py todo` | Start Todo app in development mode |
| Run Weather app | `make weather` | `python tools/dev.py weather` | Start Weather app in development mode |
| Format code | `make format` | `python tools/dev.py format` | Format code with Black and isort |
| Lint code | `make lint` | `python tools/dev.py lint` | Lint code with flake8 |
| Type check | `make typecheck` | `python tools/dev.py typecheck` | Type check with mypy |
| Run tests | `make test` | `python tools/dev.py test` | Run all tests |
| Clean artifacts | `make clean` | `python tools/dev.py clean` | Clean build artifacts |

## 🐳 Docker Deployment

Run both applications using Docker Compose:

```bash
# Set environment variables
export OPENWEATHER_API_KEY=your_api_key_here

# Start all services
docker-compose up -d

# Stop all services
docker-compose down
```

## 🌐 Production Deployment

Build applications for production:

```bash
# Build Todo app
make build-todo

# Build Weather app
make build-weather

# Or use deployment script
./scripts/deploy.sh todo production
./scripts/deploy.sh weather production
```

## 🔧 Configuration

### Todo App Configuration
- **Database**: SQLite database automatically created in `data/todo_app.db`
- **Ports**: Configurable in `apps/todo-app/rxconfig.py`

### Weather App Configuration
- **API Key**: Set `OPENWEATHER_API_KEY` in `.env` file
- **Database**: SQLite database automatically created in `data/weather_app.db`
- **Ports**: Configurable in `apps/weather-app/rxconfig.py`

## 🎨 Dark Theme

Both applications feature a consistent dark theme with:
- Deep black backgrounds (#0a0a0a)
- Subtle surface colors (#1a1a1a, #2a2a2a)
- Blue primary accent (#3b82f6)
- Green success indicators (#10b981)
- Smooth animations and hover effects

## 🧪 Testing

Run tests for all applications:

```bash
make test
# or
python tools/dev.py test
```

Individual app testing:
```bash
# Todo app tests
cd apps/todo-app && python -m pytest

# Weather app tests
cd apps/weather-app && python -m pytest
```

## 📖 API Documentation

When running in development mode, interactive API documentation is available:
- Todo App: http://localhost:8000/docs
- Weather App: http://localhost:8001/docs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Format and lint your code: `make format && make lint`
5. Run tests: `make test`
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Reflex](https://reflex.dev/) - For the amazing full-stack Python framework
- [FastAPI](https://fastapi.tiangolo.com/) - For the high-performance backend framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - For the powerful ORM
- [OpenWeatherMap](https://openweathermap.org/) - For the weather API

## 📞 Support

For questions and support:
- Create an issue on GitHub
- Check the [documentation](docs/)
- Review the example applications

---

Built with ❤️ using Python and modern web technologies.