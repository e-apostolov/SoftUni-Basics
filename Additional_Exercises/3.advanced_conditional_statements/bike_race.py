count_juniors = int(input())
count_seniors = int(input())
trace_type = input()

total_price = 0

if trace_type == "trail":
    total_price = (count_juniors * 5.50) + (count_seniors * 7.00)
elif trace_type == "cross-country":
    total_price = (count_juniors * 8.00) + (count_seniors * 9.50)
    if (count_seniors + count_juniors) >= 50:
        total_price *= 0.75
elif trace_type == "downhill":
    total_price = (count_juniors * 12.25) + (count_seniors * 13.75)
elif trace_type == "road":
    total_price = (count_juniors * 20.00) + (count_seniors * 21.50)

total_price *= 0.95

print(f"{total_price:.2f}")