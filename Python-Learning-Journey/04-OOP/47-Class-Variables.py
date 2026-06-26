# class variables = Shared among all instance of a class 
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    # class variables
    class_year = 2024
    num_students = 0
    # class variables

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age 
        # instance variables
        Student.num_students +=1

student1 = Student("Ahmed",22)
student2 = Student("Mohamed",30)
student3 = Student("Yosef",17)
student4 = Student("Basil",23)
student5 = Student("Zaid",33)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print(student5.name)
