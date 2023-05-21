budget = float(input())

while True:
    name_of_actor = input()
    if name_of_actor == "ACTION":
        break
    if len(name_of_actor) > 15:
        movie_budget = budget * 0.20
    else:
        movie_budget = float(input())
    budget -= movie_budget
    if budget <= 0:
        break

if budget > 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")

