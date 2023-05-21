from math import floor, ceil

price_tennis_racquet = float(input())
count_tennis_racquet = int(input())
count_sneakers = int(input())

sneakers_price = price_tennis_racquet / 6
total = (price_tennis_racquet * count_tennis_racquet) + (sneakers_price * count_sneakers)

total += total * 0.2

print(f"Price to be paid by Djokovic {floor(total / 8)}")
print(f"Price to be paid by sponsors {ceil(total / 8 * 7)}")