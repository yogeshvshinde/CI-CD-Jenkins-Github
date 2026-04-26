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
def index():
    """Display all students"""
    students = mongo.db.students.find()
    return render_template('index.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Add a new student"""
    if request.method == 'POST':
        mongo.db.students.insert_one({
            "name": request.form['name'],
            "email": request.form['email'],
            "course": request.form['course']
        })
        return redirect(url_for('index'))

    return render_template('add_student.html')


@app.route('/update/<student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    """Update existing student"""
    student = mongo.db.students.find_one({"_id": ObjectId(student_id)})

    if request.method == 'POST':
        mongo.db.students.update_one(
            {"_id": ObjectId(student_id)},
            {
                "$set": {
                    "name": request.form['name'],
                    "email": request.form['email'],
                    "course": request.form['course']
                }
            }
        )
        return redirect(url_for('index'))

    return render_template('update_student.html', student=student)


@app.route('/delete/<student_id>')
def delete_student(student_id):
    """Delete a student"""
    mongo.db.students.delete_one({"_id": ObjectId(student_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    # ❌ DO NOT use debug=True in production
    debug_mode = os.environ.get("FLASK_DEBUG", "False") == "True"

    app.run(host="0.0.0.0", port=5000, debug=debug_mode)