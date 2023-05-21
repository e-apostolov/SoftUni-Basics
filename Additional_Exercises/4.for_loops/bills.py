count_months = int(input())
electricity = 0
water = 0
internet = 0
others = 0
average_bill = 0

for i in range(1, count_months + 1):
    input_e = float(input())
    electricity += input_e
    water += 20
    internet += 15
    others += (input_e + 20 + 15) * 1.2
    average_bill = (electricity + water + internet + others) / i

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average_bill:.2f} lv")