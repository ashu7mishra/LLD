class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


def sort_students(students):
    # TODO: Implement the sorting logic here
    # You need to sort the students list based on the requirements:
    # 1. Sort by marks in ascending order
    # 2. If marks are the same, sort by name in alphabetical order
    sorted_students = sorted(students, key=lambda x : (x.marks, x.name))
    return sorted_students


# Example usage:
student1 = Student("Alice", 85)
student2 = Student("Bob", 75)
student3 = Student("Charlie", 85)
student4 = Student("David", 90)

students = [student1, student2, student3, student4]

sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student.name}, Marks: {student.marks}")
