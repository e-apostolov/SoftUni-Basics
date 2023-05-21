

screening_type = input()
rows = int(input())
columns = int(input())

cinema_area = rows * columns
result = 0

if screening_type == "Premiere":
    result = cinema_area * 12.00
elif screening_type == "Normal":
    result = cinema_area * 7.50
elif screening_type == "Discount":
    result = cinema_area * 5.00

print(f"{result:.2f} leva")