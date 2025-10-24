import json
import os

class CourseQueue:
    def __init__(self, filename="courses.json"):
        self.filename = filename
        self.courses = {}  # {course_name: [student_ids]}
        self.load_courses()

    def load_courses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.courses = json.load(f)
        else:
            self.courses = {}

    def save_courses(self):
        with open(self.filename, "w") as f:
            json.dump(self.courses, f, indent=4)

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = []
            self.save_courses()

    def enqueue_student(self, course_name, student_id):
        if course_name not in self.courses:
            self.add_course(course_name)
        if student_id not in self.courses[course_name]:  # prevent duplicates
            self.courses[course_name].append(student_id)
            self.save_courses()
            return True
        return False

    def get_queue(self, course_name):
        return list(self.courses.get(course_name, []))
