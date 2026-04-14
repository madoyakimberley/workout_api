#Adding Data to the database-----> done with Dennis

from app import app, db
from models import Workout, Exercise, WorkoutExercise

with app.app_context():

    #reset tables (clean start) -----> drop tables n all
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    #Same as using REPL method :)
    # Create workouts
    w1 = Workout(name="Leg Day", date="2026-04-15")
    w2 = Workout(name="Upper Body", date="2026-04-16")

    # Create exercises
    e1 = Exercise(name="Squats")
    e2 = Exercise(name="Push Ups")

    # Add to DB
    db.session.add_all([w1, w2, e1, e2])
    db.session.commit()

    # Create relationship AFTER commit (safe IDs)
    we1 = WorkoutExercise(
        workout_id=w1.id,
        exercise_id=e1.id,
        sets=4,
        reps=12
    )

    db.session.add(we1)
    db.session.commit()

    print("Database seeded successfully :)")