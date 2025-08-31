# =============================================================================
# EXERCISE 1: BASIC CLASS CREATION
# =============================================================================
"""
Create a 'Student' class with the following:
- Attributes: name, age, student_id, grades (list)
- Methods: 
  - add_grade(grade): adds a grade to the grades list
  - get_average(): returns the average of all grades
  - display_info(): prints student information
  - is_passing(): returns True if average >= 60, False otherwise
"""
# =============================================================================
# EXERCISE 1: BASIC CLASS CREATION
# =============================================================================

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        #Add the grade in the grades list
        self.grades.append(grade)

    def get_average(self):
        #Get the Average of the grades
        if not self.grades:
            return 0
        return sum(self.grades)/len(self.grades)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student id: {self.student_id}")
        print(f"Average: {self.get_average()}")
        print(f"Passing: {self.grades}")

    def is_passing(self):
        #Return True if self.get_average >= 60, otherwise
        return self.get_average() >= 60
    
#Test the student class:
student1 = Student('Fatima Ali','23','2110')
student1.add_grade(85)
student1.add_grade(98)
student1.add_grade(78)
student1.add_grade(88)

print(f"Average: {student1.get_average()}")
print(f"Passing: {student1.is_passing()}")
student1.display_info()



