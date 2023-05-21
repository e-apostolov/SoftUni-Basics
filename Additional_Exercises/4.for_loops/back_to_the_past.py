inherited_amount = float(input())
target_year = int(input())
spend_money = 0
ivan_years = 18

for i in range(1800, target_year + 1):
    if i % 2 == 0:
        spend_money += 12000
        ivan_years += 1
    else:
        spend_money += 12000 + (50 * ivan_years)
        ivan_years += 1

diff = abs(inherited_amount - spend_money)

if spend_money <= inherited_amount:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
