
n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    user_input = int(input())
    left_sum += user_input

for i in range(0, n):
    user_input = int(input())
    right_sum += user_input

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff} ")
