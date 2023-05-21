
n = int(input())
sum_numbers = 0
max_number = 0

for i in range(n):
    user_input = int(input())
    sum_numbers += user_input
    if user_input > max_number:
        max_number = user_input

sum_numbers -= max_number
if sum_numbers == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(sum_numbers - max_number)
    print("No")
    print(f"Diff = {diff}")