# schemas.py
# Handles:
# - converting data to JSON
# - validating request data

from marshmallow import Schema, fields, validate


# EXERCISE SCHEMA
class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)  # auto-generated ID
    name = fields.Str(required=True, validate=validate.Length(min=2))  # must be at least 2 chars


# WORKOUT SCHEMA
class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)  # auto ID
    name = fields.Str(required=True, validate=validate.Length(min=2))  # workout name required
    date = fields.Str(required=True)  # workout date required


# WORKOUT EXERCISE SCHEMA
class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)  # auto ID

    workout_id = fields.Int(required=True)  # must link workout
    exercise_id = fields.Int(required=True)  # must link exercise

    sets = fields.Int()  # optional
    reps = fields.Int()  # optional
    duration = fields.Int()  # optional