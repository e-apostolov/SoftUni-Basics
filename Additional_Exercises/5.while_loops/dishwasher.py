num_bottles = int(input())
remaining_detergent = num_bottles * 750
dishwasher_fill = 0
sum_dishes = 0
sum_pots = 0

while True:
    items = input()
    if items == "End":
        break
    items = int(items)
    dishwasher_fill += 1
    if dishwasher_fill % 3 == 0:
        remaining_detergent -= items * 15
        sum_pots += items
    else:
        remaining_detergent -= items * 5
        sum_dishes += items
    if remaining_detergent < 0:
        break


if remaining_detergent >= 0:
    print("Detergent was enough!")
    print(f"{sum_dishes} dishes and {sum_pots} pots were washed.")
    print(f"Leftover detergent {remaining_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(remaining_detergent)} ml. more necessary!")
