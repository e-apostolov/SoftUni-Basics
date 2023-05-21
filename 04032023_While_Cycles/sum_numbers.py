goal_sum = int(input())
total_sum = 0

while True:
    user_input = int(input())
    total_sum += user_input
    if total_sum >= goal_sum:
        break

print(total_sum)
