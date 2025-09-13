def create_student(name,age,grade):
    return (name, age, grade)

def find_top_student(students):
        if not students:
            return None
        
        top_student = max(students, key= lambda student: student[2])
        return top_student

#create students list
student1 = create_student("Alice", 15 , 89)
student2 = create_student("Fatima", 23, 78)
student3 = create_student("Ali", 26, 68)
student4 = create_student("Yusma", 23, 99)

#Create a List of students
students = [student1,student2,student3,student4]

print("All students:")
for student in students:
     name, age , grade = student
     print(f'Name: {name}, Age: {age}, Grade: {grade}')

print()

#Find top student
top_student = find_top_student(students)
if top_student:
     top_name,top_age,top_grade = top_student
     print(f"Top student: {top_name}, Top age: {top_age}, Top grade: {top_grade}")
           









        

    


