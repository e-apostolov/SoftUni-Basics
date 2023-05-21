lily_age = int(input())
w_machine_price = float(input())
toy_price = int(input())

sum_cash = 0
sum_toys = 0

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        sum_cash += ((5 * i) - 1)
    else:
        sum_toys += toy_price

total_cash = sum_cash + sum_toys

if total_cash >= w_machine_price:
    print(f"Yes! {total_cash - w_machine_price:.2f}")
else:
    print(f"No! {abs(total_cash - w_machine_price):.2f}")




