shirt_cost = float(input())
target_cost = float(input())

shorts_cost = shirt_cost * 0.75
socks_cost = shorts_cost * 0.20
boots_cost = (shirt_cost + shorts_cost) * 2
total_sum = shirt_cost + shorts_cost + socks_cost + boots_cost
total_sum -= total_sum * 0.15

diff = abs(total_sum - target_cost)
if total_sum >= target_cost:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")