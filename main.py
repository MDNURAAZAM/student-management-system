from typing import List, Dict


class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name: str = name
        self.age: int = age
        self.address: str = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


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
        self.courses: List['Course'] = []

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
                f"Congratulations. {self.name} is successfully enrolled in {course.course_name} course."
            )
        else:
            print(f"{self.name} is already enrolled in {course.course_name} course")

    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id} ")

        # show grades
        print("Grades: { ")
        for x, y in self.grades.items():
            print(f"Course: {x}: {y}")
        print(" }")

        # show courses
        print("Enrolled Courses:")
        print(f"{", ".join([course.course_name for course in self.courses])}")


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):

        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} is succesfully enrolled in {self.course_name} course")
        else:
            print(f"{student.name} is already enrolled in {self.course_name} course")

    def display_course_info(self):
        print("Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(
            "Enrolled Students:",
            ", ".join([student.name for student in self.students])
            or "No students enrolled",
        )


math_course = Course("Math", "MATH101", "Azam")
physics_course = Course("Physics", "PHY101", "Esha")

student1 = Student("Irham", 5, "cumilla", "0")
student2 = Student("Irham2", 6, "cumilla", "1")
student1.enroll_course(math_course)
student1.enroll_course(math_course)

# student1.add_grade("MATH101", "A")


# student1.enroll_course(math_course)

math_course.add_student(student1)
math_course.add_student(student2)
math_course.add_student(student2)
math_course.display_course_info()
# math_course.add_student(student2)
# math_course.add_student(student2)
