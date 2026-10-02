import os


os.system('cls' if os.name == 'nt' else 'clear')



celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32


print("================================")
print("       TEMPERATURE STATION")
print("================================")
print(f"Celsius: {celsius:.2f}°C")
print(f"Fahrenheit: {fahrenheit:.2f}°F")
print("================================")


fahrenheit_input = float(input("\nEnter temperature in Fahrenheit: "))

celsius_from_fahrenheit = (fahrenheit_input - 32) * 5 / 9

os.system('cls' if os.name == 'nt' else 'clear')



print("================================")
print("       TEMPERATURE CONVERTER")
print("================================")
print(f"Fahrenheit: {fahrenheit_input:.2f}°F")
print(f"Celsius: {celsius_from_fahrenheit:.2f}°C")
print("================================")