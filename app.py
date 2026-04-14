
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Init the Flask app
app = Flask(__name__)

# ---> DATABASE CONFIGURATION 
# Setting up our SQLite connection and keeping things efficient ;)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Linking SQLAlchemy and Flask-Migrate to the app :)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models and schemas (The blueprints for our data)
from models import Workout, Exercise, WorkoutExercise
from schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema

# Initialize schemas for turning Python objects into JSON :)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

we_schema = WorkoutExerciseSchema()

# ---> ROUTES :)

@app.route("/")
def home():
    # Simple test route to make sure we are live!
    return jsonify({"message": "Workout API running"})

# ----------------> WORKOUT ROUTES 

@app.route("/workouts", methods=["GET"])
def get_workouts():
    # Grab everything from the workouts table ;)
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts))

@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.json

    # ---> Creating a new session 
    workout = Workout(
        name=data["name"],
        date=data["date"]
    )

    db.session.add(workout)
    db.session.commit()

    return jsonify(workout_schema.dump(workout)), 201

@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    # Find it first, or throw a 404 if it doesn't exist :)
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted"}), 200

@app.route("/workouts/<int:id>", methods=["PATCH"])
def update_workout(id):
    workout = Workout.query.get_or_404(id)
    data = request.json

    # ---> Smart Update: Only change the field if it's in the request body ;)
    workout.name = data.get("name", workout.name)
    workout.date = data.get("date", workout.date)

    db.session.commit()

    return jsonify(workout_schema.dump(workout)), 200

# ----------------> EXERCISE ROUTES 

@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises))

@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.json

    # ---> Adding a new move to our library (e.g. "Deadlift")
    exercise = Exercise(name=data["name"])

    db.session.add(exercise)
    db.session.commit()

    return jsonify(exercise_schema.dump(exercise)), 201

@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted"}), 200

@app.route("/exercises/<int:id>", methods=["PATCH"])
def update_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    data = request.json

    # Keeping it flexible ;)
    exercise.name = data.get("name", exercise.name)

    db.session.commit()

    return jsonify(exercise_schema.dump(exercise)), 200

# ----------------> WORKOUT-EXERCISE ROUTE

@app.route("/workout-exercises", methods=["POST"])
def add_workout_exercise():
   
    data = request.json

    # No more shortnames! Using workout_exercise for clarity ;)
    workout_exercise = WorkoutExercise(
        workout_id=data["workout_id"],
        exercise_id=data["exercise_id"],
        sets=data.get("sets"),
        reps=data.get("reps"),
        duration=data.get("duration")
    )

    db.session.add(workout_exercise)
    db.session.commit()

    return jsonify(we_schema.dump(workout_exercise)), 201

@app.route("/workout-exercises/<int:id>", methods=["PATCH"])
def update_workout_exercise(id):
    # Find the specific entry in the join table ;)
    workout_exercise = WorkoutExercise.query.get_or_404(id)
    data = request.json

    # ---> Use .get() so we don't overwrite with 'None' if a field is missing :)
    workout_exercise.sets = data.get("sets", workout_exercise.sets)
    workout_exercise.reps = data.get("reps", workout_exercise.reps)
    workout_exercise.duration = data.get("duration", workout_exercise.duration)

    db.session.commit()

    return jsonify(we_schema.dump(workout_exercise)), 200