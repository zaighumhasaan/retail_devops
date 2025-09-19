# retail_devops Proof-of-Concept E-commerce

## Environment Setup

1. **Python & Django**
   - Python 3.10+ (recommended: 3.13)
   - Install dependencies:
     ```sh
     python -m venv .venv
     .venv\Scripts\activate
     pip install -r requirements.txt
     ```
2. **DevOps Tools**
   - Code formatting: `black`, linting: `flake8`
   - Testing: `pytest`, `pytest-django`, coverage: `coverage`
   - Containerization: see Docker instructions below

## Project Structure
- `retail_devops/` (Django project)
- `products/` (app)
- `orders/` (app)
- `users/` (app)
- `templates/` (HTML templates)
- `static/` (CSS/JS, Bootstrap/Tailwind)

## Database
- Default: SQLite (local dev)
- Production: PostgreSQL (see `.env` and `settings.py`)

## Running Locally
```sh
python manage.py migrate
python manage.py runserver
```

## Docker & Production
- See `docker-compose.yml` for containerized setup.
- PostgreSQL config via `.env` file.

## Testing & Coverage
```sh
pytest
coverage run manage.py test
coverage report
```

## Formatting & Linting
```sh
black .
flake8 .
```

## Admin
- Access Django admin at `/admin` (superuser required).

---

For more details, see comments in each app and settings file.