from typing import Dict, List


class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

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
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject: str, grade: str):
        if subject in self.courses:
            self.grades[subject] = grade
            print(f"Grade {grade} added for {self.name} in {subject} course.")
        else:
            print(f"Error: {self.name} is not enrolled in {subject} course.")

    def enroll_course(self, course: str):
        if course not in self.courses:
            self.courses.append(course)
            print(
                f"Congratulations. {self.name} is successfully enrolled in {course} course."
            )
        else:
            print(f"{self.name} is already enrolled in {course} course")

    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id} ")
        print(
            f"Enrolled Courses: {', '.join(self.courses) if self.courses else "None"} "
        )
        print("Grades: ")
        print(*(f"{x} {y}" for x, y in self.grades.items()), sep="\n")


student1 = Student("azam", 28, "cumilla", 0)
student1.add_grade("Math", "A")
student1.display_student_info()
