pairs_no = int(input())
first_pair = 0

first_number = int(input())
second_number = int(input())
sum_pair = first_number + second_number
max_diff = 0

for i in range(pairs_no - 1):
    first_number_1 = int(input())
    second_number_1 = int(input())
    sum_pair_1 = first_number_1 + second_number_1
    if sum_pair_1 != sum_pair:
        max_diff = abs(sum_pair - sum_pair_1)
    sum_pair = sum_pair_1

if max_diff == 0:
    print(f"Yes, value={sum_pair}")
else:
    print(f"No, maxdiff={max_diff}")






