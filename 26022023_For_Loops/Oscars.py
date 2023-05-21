name_of_actor = input()
default_points = float(input())
no_jury = int(input())

for i in range(no_jury):
    name_jury = input()
    points = float(input())
    default_points += (len(name_jury) * points) / 2
    if default_points > 1250.5:
        break

if default_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {default_points:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {abs(default_points-1250.5):.1f} more!")