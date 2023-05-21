x_height = float(input())
y_length = float(input())
h_height = float(input())

liter_green = 3.4
liter_red = 4.3

front_wall = (x_height * x_height) - (1.2 * 2)
back_wall = (x_height * x_height)
side_walls = (x_height * y_length) - (1.5 * 1.5)
total_walls = front_wall + back_wall + (2 * side_walls)

roof_square = x_height * y_length
roof_triangle = (x_height * h_height)/2
total_roof = (2 * roof_square) + (2 * roof_triangle)

needed_green = total_walls / 3.4
needed_red = total_roof / 4.3

print(f"{needed_green:.2f}")
print(f"{needed_red:.2f}")