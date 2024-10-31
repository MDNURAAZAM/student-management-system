from typing import List, Dict


class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name: str = name
        self.age: int = age
        self.address: str = address

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


class Student(Person):
    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        student_id: str,
    ):
        super().__init__(name, age, address)
        self.student_id: str = student_id
        self.grades: Dict = {}
        self.courses: List["Course"] = []
        print(f"Student {name} (ID: {student_id}) is added successfully.")

    def add_grade(self, course_code: str, grade: str):
        is_enrolled = [
            course for course in self.courses if course.course_code == course_code
        ]
        if len(is_enrolled) > 0:
            course = is_enrolled[0]
            self.grades[course.course_name] = grade
            print(f"Grade {grade} added for {self.name} in {course.course_name}")
        else:
            print(f"Error: {self.name} is not enrolled in {course_code} course.")

    def enroll_course(self, course: "Course"):

        if course not in self.courses:
            self.courses.append(course)
            print(
                f"Student {self.name} (ID: {self.student_id}) is enrolled in {course.course_name} (Code: {course.course_code})."
            )
        else:
            print(
                f"Student {self.name} (ID: {self.student_id}) is already enrolled in {course.course_name} (Code: {course.course_code})."
            )

    def display_student_info(self):
        print("Student Information:")
        self.display_person_info()
        print(f"ID: {self.student_id} ")

        # show courses
        print(
            f"Enrolled Courses: {", ".join([course.course_name for course in self.courses])}"
        )
        # show grades
        print(f"Grades: {self.grades}")


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []
        print(
            f"Course {course_name} (Code: {course_code}) is created with instructor {instructor}."
        )

    def add_student(self, student):

        if student not in self.students:
            self.students.append(student)
            print(
                f"{student.name} is succesfully enrolled in {self.course_name} course"
            )
        else:
            print(f"{student.name} is already enrolled in {self.course_name} course")

    def display_course_info(self):
        print("Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(
            "Enrolled Students: ",
            ", ".join([student.name for student in self.students])
            or "No students enrolled",
        )


class StudentManagementSystem:
    def __init__(self):
        self.students: Dict[str, "Student"] = {}
        self.courses: Dict[str, "Course"] = {}

    def add_new_student(self, name, age, address, student_id):
        if student_id not in self.students:
            new_student = Student(name, age, address, student_id)
            self.students[student_id] = new_student
        else:
            print(f"Error: Student: {name} (ID: {student_id}) already exists")

    def add_new_course(self, course_name, course_code, instructor):
        if course_code not in self.courses:
            new_course = Course(course_name, course_code, instructor)
            self.courses[course_code] = new_course
        else:
            print(f"Error: Course {course_name} (Code: {course_code}) already exists.")

    def enroll_student_in_course(self, student_id, course_code):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        
        if student and course :
            student.enroll_course(course)
        else:
            print("Error: Invalid student ID or course code.")

    def add_grade_for_student(self, student_id, course_code, grade):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        
        if student and course :
            student.add_grade(course_code,grade)
        else:
            print("Error: Invalid student ID or course code.")
    
    def display_student_details(self, student_id):
        student = self.students.get(student_id)
        if student:
            student.display_student_info()
        else:
            print(f"Error: Invalid Student ID: {student_id}")
    
sms = StudentManagementSystem()

sms.add_new_student("azam", 28, "abc", "0")
sms.add_new_course("Math", "Math101", "abc")

sms.enroll_student_in_course("0", "Math101")

