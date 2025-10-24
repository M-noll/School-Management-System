from student import StudentRegistry
from course import CourseQueue

# Initialize modules
students = StudentRegistry()
courses = CourseQueue()

# Load sample data once
def preload_mock_data():
    # Students
    sample_students = [
        {"student_id": "MU001", "name": "Alice", "year": 1},
        {"student_id": "MU002", "name": "Bob", "year": 2},
    ]
    for s in sample_students:
        students.add_student(s["student_id"], s["name"], s["year"])

    # Courses
    sample_courses = ["Math101", "CS101"]
    for course in sample_courses:
        courses.add_course(course)

preload_mock_data()

# --- Menu System ---
def menu():
    while True:
        print("\n--- School Management System ---")
        print("1. Add Student")
        print("2. Enroll Student in Course")
        print("3. View Course Queue")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            sid = input("Student ID: ").strip()
            name = input("Name: ").strip()
            year = int(input("Year: ").strip())
            if students.add_student(sid, name, year):
                print(f"Student {sid} added successfully!")
            else:
                print(f"Student {sid} already exists.")

        elif choice == "2":
            sid = input("Student ID: ").strip()
            if not students.student_exists(sid):
                print("Student does not exist.")
                continue
            course_name = input("Course Name: ").strip()
            if courses.enqueue_student(course_name, sid):
                print(f"{sid} enrolled in {course_name}.")
            else:
                print(f"{sid} already enrolled in {course_name}.")

        elif choice == "3":
            course_name = input("Course Name: ").strip()
            print(f"{course_name} queue: {courses.get_queue(course_name)}")

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
