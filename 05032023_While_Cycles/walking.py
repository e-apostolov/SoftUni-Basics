goal = 10000
total_steps = 0


while True:
    count_steps = input()
    if count_steps == "Going home":
        count_steps = int(input())
        total_steps += count_steps
        break
    count_steps = int(count_steps)
    total_steps += int(count_steps)
    if total_steps >= goal:
        break

diff = abs(total_steps - goal)
if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")


