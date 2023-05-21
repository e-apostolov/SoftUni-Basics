available_budget = float(input())
category = input()
group_members = int(input())

tickets_price = 0

if category == "VIP":
    tickets_price = group_members * 499.99
elif category == "Normal":
    tickets_price = group_members * 249.99

if 1 <= group_members <= 4:
    tickets_price += available_budget * 0.75
elif 5 <= group_members <= 9:
    tickets_price += available_budget * 0.6
elif 10 <= group_members <= 24:
    tickets_price += available_budget * 0.5
elif 25 <= group_members <= 49:
    tickets_price += available_budget * 0.4
else:
    tickets_price += available_budget * 0.25

diff = abs(tickets_price - available_budget)

if tickets_price <= available_budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
