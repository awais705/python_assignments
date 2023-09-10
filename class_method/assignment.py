"""
In this exercise, you will create a Python class named Student to represent students. 
The class should have the following attributes and methods:

Attributes:

name: instance variable
age: instance variable
courses: instance variable
available_courses: class variable -> possible values ["English", "Urdu", "Physics", "Math", "Chemistry"]

Methods:

display_info(): An instance method that displays the student's name and age.
enroll(): An instance method that allows a student to enroll in a course by adding it to their list of enrolled courses.
list_courses(): An instance method that displays all the courses that student is enrolled
list_available_courses(): An instance method that display all the avaiable courses


1. Create three instances of the Student class with different names and ages.

2. enroll the students in courses by calling the enroll method.
make sure student should only enroll in the course that are listing in available course
i.e if user input the course "Islamyat" then program should not allow it

3. call list_courses
4. call list_available_courses
"""


class Student:
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]

    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses


# display_info(): An instance method that displays the student's name and age.


    def display_info(self):
        return "Student name is " + self.name + "  and age is " + str(self.age)


# enroll(): An instance method that allows a student to enroll in a course by adding it to their list of enrolled courses.


    def enroll(self, course):

        if course.capitalize() in Student.available_courses:
            self.courses.append(course)
            return course + " Added succesfully!"
        else:
            return course + " is not available. Please try again"


# list_courses(): An instance method that displays all the courses that student is enrolled

    def list_courses(self):
        return self.name + " enrolled in " + ",".join(self.courses)


# list_available_courses(): An instance method that display all the avaiable courses

    def list_available_courses(self):
        available_courses = set(Student.available_courses) - set(self.courses)
        return "Available courses for " + self.name + " are " + ",".join(available_courses)


# 1. Create three instances of the Student class with different names and ages.
student1 = Student("Muhammad Awais", 32, [])
student2 = Student("Siraj Munir", 30, [])
student3 = Student("Faraz Ahmed", 28, [])


# 2. enroll the students in courses by calling the enroll method.
# make sure student should only enroll in the course that are listing in available course
# i.e if user input the course "Islamyat" then program should not allow it

print(student1.enroll("Urdu"))
print(student2.enroll("English"))
print(student3.enroll("chemistry"))

print(student1.enroll("Chemistry"))
print(student2.enroll("Urdu"))
print(student3.enroll("English"))


# 3. call list_courses
# student1.enroll("Islamiat")
print(student1.list_courses())
print(student2.list_courses())
print(student3.list_courses())

# 4. call list_available_courses

print(student1.list_available_courses())
print(student2.list_available_courses())
print(student3.list_available_courses())
