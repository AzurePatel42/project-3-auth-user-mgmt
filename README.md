# patel-auth-user-mgmt

⚠️ Legacy authentication service

Superseded by:

👉 patel-auth-service-framework
A production‑ready FastAPI microservice for secure user authentication and management.
This service provides JWT‑based login, password hashing, user registration, and PostgreSQL integration, all packaged inside a clean, scalable architecture and fully containerized with Docker.

🚀 Features
User Registration with hashed passwords (bcrypt)

JWT Authentication (access tokens)

Secure Password Hashing using passlib

PostgreSQL + SQLAlchemy ORM

Environment‑based configuration using Pydantic Settings

Dockerized for consistent deployment

Clean, scalable project structure

Auto‑generated API docs via Swagger UI

🧱 Tech Stack
FastAPI

Python 3.11

SQLAlchemy ORM

PostgreSQL

Pydantic v2 + Pydantic Settings

Python‑Jose (JWT)

Docker & Docker Compose

📂 Project Structure
Code
app/
│
├── auth/
│   ├── routes.py          # Register & Login endpoints
│   ├── models.py          # User database model
│   ├── schemas.py         # Pydantic schemas for auth
│   ├── hashing.py         # Password hashing utilities
│   └── jwt_handler.py     # JWT creation & validation
│
├── core/
│   └── config.py          # Environment variables & settings
│
├── users/
│   ├── models.py          # (Future expansion)
│   └── schemas.py         # (Future expansion)
│
├── database.py            # SQLAlchemy engine & session
└── main.py                # FastAPI app entrypoint
🔌 API Endpoints
Auth
Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	Login and receive JWT


Default
Method	Endpoint	Description
GET	/	Health check


🐳 Running with Docker
1. Build the containers
Code
docker compose build --no-cache
2. Start the services
Code
docker compose up
3. Open API Docs
Code
http://localhost:8000/docs
🧪 Example Requests
Register
Code
POST /auth/register
{
  "email": "test@example.com",
  "password": "123456"
}
Login
Code
POST /auth/login
{
  "email": "test@example.com",
  "password": "123456"
}
🔮 Future Enhancements
User profile CRUD

Role‑based access control (RBAC)

Refresh tokens

Admin dashboard endpoints

Email verification

Password reset flow

📜 License
This project is open‑source and available under the MIT License.
