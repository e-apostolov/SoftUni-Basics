from math import floor

no_of_tournaments = int(input())
initial_points = int(input())
points = 0
tournaments_won = 0


for i in range(no_of_tournaments):
    result = input()
    if result == "W":
        points += 2000
        tournaments_won += 1
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720

total_points = points + initial_points

print(f"Final points: {total_points}")
print(f"Average points: {floor(points / no_of_tournaments)}")
print(f"{tournaments_won / no_of_tournaments * 100:.2f}%")

