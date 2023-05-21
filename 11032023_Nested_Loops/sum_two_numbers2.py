start_num, end_num = int(input()), int(input())
magic_num = int(input())

is_found = False

for first_num in range(start_num, end_num +1):
    for second_num in range(start_num, end_num +1):
        if first_num + second_num == magic_num:
            combinations = (first_num - start_num) * (end_num - start_num + 1) + (second_num - start_num + 1)
            print(f"Combination N:{combinations} ({first_num} + {second_num} = {magic_num})")
            is_found = True

    if is_found:
        break

else:
    combinations = (end_num - start_num + 1) ** 2
    print(f"{combinations} combinations - neither equals {magic_num}")