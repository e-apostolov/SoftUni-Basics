from math import pi

figure_type = input()

if figure_type == "square":
    a = float(input())
    print(f"{a * a:.3f}")
elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    print(f"{a * b:.3f}")
elif figure_type == "circle":
    r = float(input())
    print(f"{(r ** 2) * pi:.3f}")
elif figure_type == "triangle":
    a = float(input())
    ha = float(input())
    print(f"{(a * ha) / 2:.3f}")