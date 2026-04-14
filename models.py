from app import db

# --- >WORKOUT MODEL
# ---> The "Main Event" (like "Leg Day" or "Morning Yoga")
class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

    # ---> Connection to the join table
    # Using cascade="all, delete" so if a workout is gone, the entries go too :)
    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete"
    )


# ---> EXERCISE MODEL
# ---> Our "Library" of moves (Bench Press, Squats, etc.)
class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    # unique=True so we don't have the same exercise twice in the list ;)
    name = db.Column(db.String, nullable=False, unique=True)

    # ---> Links back to the join table logic
    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete"
    )


# --->WORKOUT_EXERCISE MODEL (The Join Table)<as we were taught today>
# ---> This links Workouts and Exercises together! 
# It's where we store the actual reps and sets for a session :)
class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    # ---> Foreign Keys: These point to the IDs in the other tables
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"), nullable=False)

    # Stats for the specific set ;)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    duration = db.Column(db.Integer) 

    # ---> Relationships: Allows us to hop between objects easily in Python
    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")