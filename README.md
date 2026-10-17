# Task Management API

A REST API built with Python, FastAPI, and PostgreSQL to create, view, update, complete, and delete tasks.

## Technologies

- Python
- FastAPI
- PostgreSQL
- Psycopg
- Pydantic

## Features

- Create and retrieve tasks
- Update task titles
- Mark tasks as complete
- Delete tasks
- Store tasks in PostgreSQL

## Project Structure

    cli-todo-app/
    ├── .gitignore
    ├── app.py
    ├── database.py
    ├── README.md
    ├── requirements.txt
    └── task.py

## Installation

Clone the repository:

    git clone https://github.com/sheamnur/cli-todo-app.git
    cd cli-todo-app

Install dependencies:

    pip install -r requirements.txt

Configure your PostgreSQL credentials in a `.env` file.

Create the database and required table, then start the API:

    uvicorn app:app --reload

## API Documentation

Once the server is running, open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Author

Sheam Nur

GitHub: https://github.com/sheamnur