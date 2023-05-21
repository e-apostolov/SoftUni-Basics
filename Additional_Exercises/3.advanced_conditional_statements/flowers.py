count_x = int(input())
count_r = int(input())
count_l = int(input())
season = input()
holiday = input()

price_x = 0
price_r = 0
price_l = 0
total_price = price_x + price_r + price_l

if season == "Spring" or season == "Summer":
    price_x = count_x * 2.00
    price_r = count_r * 4.10
    price_l = count_l * 2.50
elif season == "Autumn" or season == "Winter":
    price_x = count_x * 3.75
    price_r = count_r * 4.50
    price_l = count_l * 4.15

total_price = price_x + price_r + price_l
if holiday == "Y":
    total_price *= 1.15

if count_l >= 7 and season == "Spring":
    total_price *= 0.95
elif count_r >= 10 and season == "Winter":
    total_price *= 0.90
if (count_x + count_r + count_l) > 20:
    total_price *= 0.80

total_price += 2.00

print(f"{total_price:.2f}")

