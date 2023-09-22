# Define a class to represent a student object
class Student:
    # Initialize the attributes of the student object
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    # Define a string representation of the student object
    def __str__(self):
        return f"{self.name} ({self.roll_number}), CGPA: {self.cgpa}"

# Define a function to sort a list of student objects based on their CGPA in descending order
def sort_students(students):
    # Use the built-in sorted function with a custom key function that returns the cgpa attribute of each student object
    # Use the reverse parameter to sort in descending order
    return sorted(students, key=lambda student: student.cgpa, reverse=True)

# Test the function with different input lists of students
students1 = [Student("siddharth", "19CS001", 9.5), Student("thilak", "19CS002", 8.7), Student("mano", "19CS003", 7.8)]
students2 = [Student("sridhar", "19CS004", 8.9), Student("stephen raj", "19CS005", 9.2), Student("buvi", "19CS006", 8.4)]
students3 = [Student("abi", "19CS007", 9.1), Student("jagadeep", "19CS008", 7.6), Student("praveen", "19CS009", 8.2)]

# Print the sorted lists of students
print("Sorted list of students 1:")
for student in sort_students(students1):
    print(student)

print("Sorted list of students 2:")
for student in sort_students(students2):
    print(student)

print("Sorted list of students 3:")
for student in sort_students(students3):
    print(student)
  