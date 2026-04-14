# Workout API (Flask + SQLAlchemy)

## Project Description

This is a backend API for a workout tracking application. It allows
trainers to: - Create and manage workouts - Create and manage
exercises - Add exercises to workouts with sets, reps, or duration

Built using Flask, SQLAlchemy, and Marshmallow.

---

## Installation Instructions

1.  Clone the repository: git clone `https://github.com/madoyakimberley/workout_api`{=html} cd
    workout-api

2.  Install dependencies: pipenv install

3.  Activate virtual environment: pipenv shell

4.  Run migrations: flask db init flask db migrate -m "initial
    migration" flask db upgrade

5.  Seed the database: python seed.py

---

## Run the Application

flask run

---

## API Endpoints

### Workouts

- GET /workouts
- POST /workouts
- DELETE /workouts/`<id>`{=html}

### Exercises

- GET /exercises
- POST /exercises
- DELETE /exercises/`<id>`{=html}

### Workout Exercises

- POST /workout_exercises

---

## Project Structure

```text
workout-api/
├── migrations/
├── app.py
├── models.py
├── schemas.py
├── seed.py
└── Pipfile
```
---

## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow

---

## Notes

- Includes model, schema, and table-level validations
- Uses RESTful API conventions
- Designed for scalability and maintainability

---

## Author

Kimberley Madoya :)
