# iBlog API

A Flask-based RESTful API and web application for managing blog posts with user authentication. Users can register, log in, create, read, update, and delete posts through a responsive web interface or API. The backend uses Flask, SQLAlchemy, JWT, and Argon2, while the frontend leverages JavaScript for API communication and Bootstrap for styling.

## Features

- **User Management**:
  - Register and log in with email and password.
  - JWT-based authentication with access and refresh tokens.
- **Post Management**:
  - Create, read, update, and delete blog posts (title, subtitle, body).
  - Posts are tied to authenticated users.
- **Web Interface**:
  - Templates for home, post creation, viewing, editing, login, and registration.
  - JavaScript for API calls, token management, and form handling.
- **Database**:
  - SQLite for local development (`data/blogs-collection.db`).
  - PostgreSQL support for production.
- **Security**:
  - Password hashing with Argon2.
  - Input validation with Marshmallow.
- **Deployment**:
  - Configured for Heroku or Docker with Gunicorn.


## Prerequisites

- Python 3.8+
- pip
- Virtualenv (recommended)
- Docker (optional, for containerization)
- Heroku CLI (optional, for Heroku deployment)
- Git

## Setup Instructions

### 1. Clone the Repository

```bash

git clone <repository-url>
cd 57-Blog_Api