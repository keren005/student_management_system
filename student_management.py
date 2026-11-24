
# Student Management System
# Student Class Diagram Implementation

# Create the Student class
class Student:

    # Constructor to initialize student information
    def __init__(self, student_id, name, age, email, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.course = course

    # Method to display student details
    def display_details(self):
        print("\n--- Student Details ---")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Course:", self.course)

    # Method to update student email
    def update_email(self, new_email):
        self.email = new_email
        print("Email address updated successfully.")

    # Method to register student for a course
    def register_for_course(self, course_name):
        self.course = course_name
        print("Student registered for", course_name)


# Create a student object
student1 = Student(
    20236380,
    "Keren Niyomuco",
    20,
    "kerenniyomuco@gmail.com",
    "Software Engineering"
)

# Display the original student information
student1.display_details()

# Update the student's email
student1.update_email("kerenniyomuco@gmail.com")

# Register the student for another course
student1.register_for_course("Data Structures")

# Display the updated student information
print("\n--- Updated Student Details ---")
student1.display_details()
