chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
fixed_cost_delivery = 2.50

chicken_menu_qty = int(input())
fish_menu_qty = int(input())
vegan_menu_qty = int(input())

price_chicken_menu = chicken_menu * chicken_menu_qty
price_fish_menu = fish_menu * fish_menu_qty
price_vegan_menu = vegan_menu * vegan_menu_qty
total_sum = (price_chicken_menu + price_fish_menu + price_vegan_menu)
total_sum = total_sum + (total_sum * 20 / 100) + fixed_cost_delivery

print(total_sum)
