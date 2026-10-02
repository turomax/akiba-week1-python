import os

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width
perimeter = 2 * (length + width)


os.system("cls" if os.name == "nt" else "clear")

len_str = f"{length:.2f}".rstrip("0").rstrip(".")
wid_str = f"{width:.2f}".rstrip("0").rstrip(".")
area_str = f"{area:.2f}".rstrip("0").rstrip(".")
perim_str = f"{perimeter:.2f}".rstrip("0").rstrip(".")

card_width = 30

print("+" + "-" * card_width + "+")
print(f"|{'RECTANGLE WORKSHOP':^{card_width}}|")
print("+" + "-" * card_width + "+")
print(f"| Length: {len_str + ' m':<{card_width - 9}}|")
print(f"| Width: {wid_str + ' m':<{card_width - 8}}|")
print(f"| Area: {area_str + ' m²':<{card_width - 7}}|")
print(f"| Perimeter: {perim_str + ' m':<{card_width - 12}}|")
print("+" + "-" * card_width + "+")