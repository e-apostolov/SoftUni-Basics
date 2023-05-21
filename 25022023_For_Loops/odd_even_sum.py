
n = int(input())

sum_odd = 0
sum_even = 0

for i in range(0, n):
    user_input = int(input())
    if i % 2 == 0:
        sum_even += user_input
    else:
        sum_odd += user_input

diff = abs(sum_even - sum_odd)

if sum_even == sum_odd:
    print(f"Yes\nSum = {sum_even}")
else:
    print(f"No\nDiff = {diff}")