import json
import os

class StudentRegistry:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}  # {student_id: {name, year}}
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.students = json.load(f)
        else:
            self.students = {}

    def save_students(self):
        with open(self.filename, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, student_id, name, year):
        if student_id in self.students:
            return False  # Student already exists
        self.students[student_id] = {"name": name, "year": year}
        self.save_students()
        return True

    def student_exists(self, student_id):
        return student_id in self.students

    def get_student(self, student_id):
        return self.students.get(student_id, None)
