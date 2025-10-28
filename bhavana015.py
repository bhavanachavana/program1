class Student:
    def __init__(self, name, roll_number, age, grade):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grade = grade

    def display_details(self):
        print("----- Student Details -----")
        print(f"Name       : {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Age        : {self.age}")
        print(f"Grade      : {self.grade}")
        print("---------------------------")
student1 = Student("Alice", 101, 20, "A")
student2 = Student("Bob", 102, 19, "B+")

 
student1.display_details()
student2.display_details()
