from math import ceil, floor

travel_duration = int(input())
food_left = int(input())
dog_food_needed = float(input())
cat_food_needed = float(input())
turtle_food_needed = float(input())

total_food_needed = travel_duration * (dog_food_needed + cat_food_needed + (turtle_food_needed * 0.001))

diff_food = abs(food_left - total_food_needed)

if food_left >= total_food_needed:
    print(f"{floor(diff_food)} kilos of food left.")
else:
    print(f"{ceil(diff_food)} more kilos of food are needed.")


