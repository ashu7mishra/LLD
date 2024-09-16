
# User Management System
## Problem Statement
You are tasked with creating a Python class hierarchy for managing users, including students and employees. The system should encapsulate the functionality required for storing and displaying user information, as well as specialized information for students and employees.

## Requirements

1.User class:
- Attributes: _username, _email
- Methods:
    - __init__(self, username, email): Constructor to initialize the user's username and email.
    - displayInfo(self): Prints the user's username and email.
    - getUsername(self): Returns the user's username.
    - getEmail(self): Returns the user's email.
    
2.Student class (derived from User):
- Attributes: _studentId, _course
- Methods:
    - __init__(self, username, email, studentId, course): Constructor to initialize the student's username, email, student ID, and course.
    - displayInfo(self): Prints the student's username, email, student ID, and course.
    - getStudentId(self): Returns the student's ID.
    - getCourse(self): Returns the student's course.
    
3.Employee class (derived from User):
- Attributes: _employeeId, _department
- Methods:
    - __init__(self, username, email, employeeId, department): Constructor to initialize the employee's username, email, employee ID, and department.
    - displayInfo(self): Prints the employee's username, email, employee ID, and department.
    - getEmployeeId(self): Returns the employee's ID.
    - getDepartment(self): Returns the employee's department.

## Display Format: 

- For both the User and Student classes, the displayInfo() method should print the information in the following format:
    - Username: [username]
    - Email: [email]
    
- For the Student class, additional information should be displayed as follows:
    - Student ID: [studentId]
    - Course: [course]

## Instructions
- Implement the User, Student, and Employee classes according to the specified requirements.
- Ensure that the Student and Employee classes inherit from the User class and override the necessary methods.
- Follow the specified display format for printing user and student information.


