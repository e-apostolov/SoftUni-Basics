km_count = int(input())
time_of_day = input()


taxi_rate = 0.70 + 0.79 * km_count
if time_of_day == "night":
    taxi_rate = 0.70 + 0.90 * km_count

bus_rate = 0.09 * km_count
train_rate = 0.06 * km_count


if km_count < 20:
    print(f"{taxi_rate:.2f}")
elif 20 <= km_count < 100:
    print(f"{bus_rate:.2f}")
else:
    print(f"{train_rate:.2f}")


