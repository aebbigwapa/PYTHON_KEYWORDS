# Student Management System

# Importing necessary modules
import random  # 'import' is used to include external modules

# Global variables
global students  # 'global' declares a global variable
students = {"Kurt_andrew": {"password": "password123", "courses": {}, "grades": {}}}
courses = ["Math", "Science", "History", "English", "Computer Science"]

def authenticate():  # 'def' defines a function
    """Authenticate student login"""
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in students and students[username]["password"] == password:  # 'if' checks a condition, 'and' is a logical operator
        print("Login successful!")
        return username  # 'return' exits the function and returns a value
    else:  # 'else' executes when 'if' condition is false
        print("Login failed!")
        return None  # 'None' represents the absence of a value

def enroll_course(username):
    """Enroll a student in a course"""
    print("Available courses:", ", ".join(courses))
    course = input("Enter course name: ")
    if course in students[username]["courses"]:  # 'in' checks membership in a list/dictionary
        print("Already enrolled!")
    elif course in courses:  # 'elif' is short for 'else if'
        students[username]["courses"][course] = "Enrolled"
        print(f"Successfully enrolled in {course}")
    else:
        print("Invalid course!")

def view_courses(username):
    """View student's enrolled courses"""
    print("Your Enrolled Courses:")
    if students[username]["courses"]:  # Checking if dictionary is not empty
        for course, status in students[username]["courses"].items():  # 'for' loops through a sequence
            print(f"{course}: {status}")
    else:
        print("No courses enrolled.")

def add_grade(username):
    """Assign a grade to a course"""
    course = input("Enter course name: ")
    if course in students[username]["courses"]:
        grade = int(input("Enter grade: "))
        students[username]["grades"][course] = grade
        print(f"Grade added for {course}: {grade}")
    else:
        print("Course not found or not enrolled")

def add_student():
    """Register a new student"""
    username = input("Enter new student username: ")
    if username in students:
        print("Username already exists!")
    else:
        password = input("Enter password: ")
        students[username] = {"password": password, "courses": {}, "grades": {}}
        print("Student added successfully!")

def main():
    """Main function to run the student management system"""
    while True:  # 'while' creates a loop that runs indefinitely until broken
        print("\nStudent Management System:")
        print("1. Login as Student")
        print("2. Register New Student")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            username = authenticate()
            if username:
                while True:
                    print("\nStudent Menu:")
                    print("1. Enroll in Course")
                    print("2. View Courses")
                    print("3. Add Grade")
                    print("4. Logout")
                    
                    student_choice = input("Enter your choice: ")
                    if student_choice == "1":
                        enroll_course(username)
                    elif student_choice == "2":
                        view_courses(username)
                    elif student_choice == "3":
                        add_grade(username)
                    elif student_choice == "4":
                        print("Logging out...")
                        break  # 'break' exits the loop
                    else:
                        print("Invalid choice! Please try again.")
        elif choice == "2":
            add_student()
        elif choice == "3":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":  # 'if' checks if the script is run directly
    main()  # Calls the main function
