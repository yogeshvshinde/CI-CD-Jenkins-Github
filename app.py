from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# -------------------------------
# Configuration
# -------------------------------

# Use environment variables (from Docker/Jenkins)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://mongodb:27017/mydb")
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

# Initialize Mongo (NO TLS for local Docker Mongo)
mongo = PyMongo(app)

# -------------------------------
# Routes
# -------------------------------

# Home page -> list students
@app.route('/')
def index():
    students = mongo.db.students.find()
    return render_template('index.html', students=students)


# Add student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        mongo.db.students.insert_one({
            "name": name,
            "email": email,
            "course": course
        })

        return redirect(url_for('index'))

    return render_template('add_student.html')


# Update student
@app.route('/update/<student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    student = mongo.db.students.find_one({"_id": ObjectId(student_id)})

    if request.method == 'POST':
        new_name = request.form['name']
        new_email = request.form['email']
        new_course = request.form['course']

        mongo.db.students.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": {
                "name": new_name,
                "email": new_email,
                "course": new_course
            }}
        )

        return redirect(url_for('index'))

    return render_template('update_student.html', student=student)


# Delete student
@app.route('/delete/<student_id>')
def delete_student(student_id):
    mongo.db.students.delete_one({"_id": ObjectId(student_id)})
    return redirect(url_for('index'))


# -------------------------------
# DevOps Health Check (IMPORTANT)
# -------------------------------
@app.route('/health')
def health():
    try:
        mongo.db.command("ping")
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


# -------------------------------
# Run App
# -------------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)