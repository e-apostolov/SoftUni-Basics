fixed_price_nylon = 1.50
fixed_price_paint = 14.50
fixed_price_paint_thinner = 5.00
fixed_price_bag = 0.40

nylon_qty = int(input())
paint_qty = int(input())
thinner_qty = int(input())
worker_hours = int(input())

sum_nylon = (nylon_qty + 2) * fixed_price_nylon
sum_paint = (paint_qty + (paint_qty * 10/100)) * fixed_price_paint
sum_paint_thinner = (thinner_qty * fixed_price_paint_thinner)

total_costs = sum_nylon + sum_paint + sum_paint_thinner + fixed_price_bag
total_sum_workers = (total_costs * 30/100) * worker_hours
print(total_costs + total_sum_workers)

