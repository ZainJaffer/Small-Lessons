class Student:

    def __init__(self, name, age, grade):
        self.subjects = []
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return self.name, self.age, self.grade, self.subjects

class StudentManager:

    def __init__(self):
        self.student_dict = {}

    def add_student(self):
        student_name = input("What is the name of your student?").title()
        student_age = int(input(f"What is the age of {student_name}?"))
        student_grade = input(f"What is the grade of {student_name}?")
        
        student_object = Student(student_name,student_age,student_grade)
        
        self.student_dict[student_object.name] = student_object

        multiple_subjects = True
        
        while multiple_subjects:
            student_subjects = input(f"What are the subjects that {student_name} studies?. Type 'stop' once you have no more subjects to add").title()
            if student_subjects == 'Stop':
                multiple_subjects = False
            else: 
                student_object.subjects.append(student_subjects)
                print(f"{student_subjects} added")
            
    def view_students(self):
        for key, value in self.student_dict.items():
            print(f"{key}: {value.age} years old, Grade: {value.grade}, Subjects: {value.subjects}")
        if not self.student_dict:
            print("There are no students to view")

    def remove_students(self):
        student_name = input("What is the name of the student you want to remove?").title()
        if student_name in self.student_dict:
            del self.student_dict[student_name]
            print(f"{student_name} succesfully removed")
        else:
            print("Sorry, this student doesn't exist")

    def update_student(self):

        student_name = input("What is the name of the student you want to update?").title()
        if student_name in self.student_dict:
            student = self.student_dict[student_name]
            print(f"{student_name} has been located, here are their details: \n {student.name}, {student.age} years old, Grade: {student.grade}, Subjects: {student.subjects}")
            action = input("What do you want to change. Type 'name', 'age', 'grade' or 'subjects' ")
            if action == 'name':
                change = input("What is the new value?")
                student.name = change
                del self.student_dict[student_name].name
                self.student_dict[student_name].name = change
        else: print("Sorry this student doesn't exist")

#TO LEARN - Not understandnig howt o change a key or value in a dictionary, for updating.... need to do more problem sets for this part...



"""
Remove the old key-value pair from the dictionary.
Insert a new key-value pair with the updated name.
"""

    # def update_student(self):
    #     attributes = ['name','age','grade','subjects']
        
    #     student_name = input("What is the name of the student you want to update?").title()
    #     if student_name in self.student_dict:
    #         student = self.student_dict[student_name]
    #         print(f"{student_name} has been located, here are their details: \n {student.name}, {student.age} years old, Grade: {student.grade}, Subjects: {student.subjects}")
    #         action = input("What do you want to change. Type 'name', 'age', 'grade' or 'subjects' ")
    #         if action in attributes:
    #             change = input("What is the new value? Warning this will replace the old value")
    #             student[action] = change
    #     else: print("Sorry this student doesn't exist")



platform = StudentManager()

# Test code, to manually add object 

zain = Student('Zain', 45, 'A')
zain.subjects.extend(['Math', 'Science', 'History', 'English']) 
platform.student_dict[zain.name] = zain

# Test code to manually call functions 

platform.view_students()
platform.update_student()
platform.view_students()


def main_flow():
    pass

main_flow()


#TODO: Split input functionality into main_flow() function
#TODO: Implement setattr for main_flow to operate efficiently
#TODO: Implement input validation
#TODO: Implement isinstance
#TODO: Implememt try and except 