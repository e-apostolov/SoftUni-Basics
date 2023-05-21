number_a = int(input())
number_b = int(input())
max_num_password = int(input())

for A in range(35, 55 + 1):
    for B in range(64, 96 + 1):
        for x in range(1, number_a + 1):
            for y in range(1, number_b + 1):
                max_num_password -= 1
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                if max_num_password <= 0 or (x == number_a and y == number_b):
                    exit()
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64