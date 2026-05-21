## 📂 Project Structure

```
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
```