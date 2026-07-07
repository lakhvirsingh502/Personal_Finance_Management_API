# Personal Finance Manager API

A RESTful API built with FastAPI for managing users and expenses.

## Features

- User management
- Expense tracking
- SQLite database
- SQLAlchemy ORM
- Pydantic validation
- Jwt Authentication.
- Role based access.
- Pagination
- Filteration
- Sort

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

- jose
=======
- jwt

- bcrypt

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Documentation

Visit:

```
http://127.0.0.1:8000/docs
```

## Project Structure
Personal_Finance_Management_Api
├── main.py
│
├── core/
│   ├── database.py
│   ├── security.py
│
├── models/
│   ├── user.py
│   ├── expense.py
│
├── schemas/
│   ├── user.py
│   ├── expense.py
│
├── routers/
│   ├── auth.py
│   ├── expenses.py
│
├── dependencies/
│   ├── get_user.py
│
├── requirements.txt
└── README.md
