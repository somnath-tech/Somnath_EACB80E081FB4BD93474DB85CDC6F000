
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

def input_students():
    student_list = []
    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        roll_number = input("Enter roll number: ")
        cgpa = float(input("Enter CGPA: "))
        student = Student(name, roll_number, cgpa)
        student_list.append(student)
    return student_list


if __name__ == "__main__":
    print("Enter student details. Enter 'q' to stop.")
    students = input_students()
    sorted_students = sort_students(students)
    
    print("\nSorted students by CGPA (descending order):")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
