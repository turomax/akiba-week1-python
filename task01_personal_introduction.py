import os


print("========================================")
print("        STUDENT INTRODUCTION            ")  
print("========================================")

Name = input("enter your full name: ")
age = int(input("enter your age: "))
city = input("enter your city location: ")
university = input("enter your university: ")
department = input("enter your department: ")
language = input("enter your programming language: ")
goal = input("enter your goal that you want to achieve: ")

os.system("cls" if os.name == "nt" else "clear")


print("========================================")
print("        STUDENT INTRODUCTION            ")  
print("========================================")

print()
 
print(f"My name is {Name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"I study {department} at {university}.")
print(f"My favourite programming language is {language}.")
print(f"My programming goal is {goal}.")

print()

print("========================================")