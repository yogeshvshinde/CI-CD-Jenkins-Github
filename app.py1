from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import os


app = Flask(__name__)

# Get Mongo URI from environment variable
mongo_uri = os.environ.get("MONGO_URI")

if not mongo_uri:
    raise Exception("MONGO_URI environment variable not set!")

# Configure MongoDB
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


# Initialize PyMongo

mongo = PyMongo(app)

# -------------------------------
# Routes
# -------------------------------

@app.route('/')
def home():
    return """
    <h1>Flask CI/CD Pipeline 🚀</h1>
    <p>MongoDB Connected Successfully</p>
    <p>Try /students endpoint</p>
    """


# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    try:
        students = list(mongo.db.students.find({}, {"_id": 0}))
        return jsonify(students)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Add a student
@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json

        if not data or "name" not in data:
            return jsonify({"error": "Name is required"}), 400

        mongo.db.students.insert_one({
            "name": data["name"],
            "age": data.get("age", None)
        })

        return jsonify({"message": "Student added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Health check (important for DevOps)
@app.route('/health', methods=['GET'])
def health():
    try:
        # simple DB ping
        mongo.db.command("ping")
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)