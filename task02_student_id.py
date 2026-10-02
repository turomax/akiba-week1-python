import os

name = input("Enter student name: ")
student_id = input("Enter student ID: ")
department = input("Enter department: ")
year = int(input("Enter year: "))
university = input("Enter university: ")
phone = input("Enter phone number: ")

os.system('cls' if os.name == 'nt' else 'clear')


width = 32

print("+" + "-" * width + "+")
print(f"|{'AKIBA STUDENT CARD':^{width}}|")
print("+" + "-" * width + "+")
print(f"| Name: {name:<{width - 8}}|")
print(f"| ID: {student_id:<{width - 6}}|")
print(f"| Department: {department:<{width - 14}}|")
print(f"| Year: {str(year):<{width - 8}}|")
print(f"| University: {university:<{width - 14}}|")
print(f"| Phone: {phone:<{width - 9}}|")
print("+" + "-" * width + "+")