price_vegetables = float(input())
price_fruits = float(input())
kg_veg = int(input())
kg_fruit = int(input())

total = (price_vegetables * kg_veg) + (price_fruits * kg_fruit)
total /= 1.94

print(f"{total:.2f}")