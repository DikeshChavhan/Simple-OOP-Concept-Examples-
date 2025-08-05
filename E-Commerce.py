from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_details(self):
        pass

# Encapsulation & Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id  # Private variable
        self.__grades = []              # Encapsulated list

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Invalid grade!")

    def calculate_average(self):
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0

    def get_details(self):  # Polymorphism
        return f"Student: {self.name}, ID: {self.__student_id}, Avg: {self.calculate_average():.2f}"

# Inheritance
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_details(self):  # Polymorphism
        return f"Teacher: {self.name}, Subject: {self.subject}"

# Object Creation
student1 = Student("Dikesh", 21, "S123")
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(76)

teacher1 = Teacher("Mrs. Sharma", 40, "Mathematics")

# Output
print(student1.get_details())  # Polymorphic call
print(teacher1.get_details())  # Polymorphic call
