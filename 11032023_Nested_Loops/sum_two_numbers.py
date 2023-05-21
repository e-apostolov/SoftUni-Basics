start_num = int(input())
end_num = int(input())
magic_num = int(input())

combinations = 0
is_found = False

for first_num in range(start_num, end_num +1):
    for second_num in range(start_num, end_num +1):
        combinations += 1

        if first_num + second_num == magic_num:
            print(f"Combination N:{combinations} ({first_num} + {second_num} = {magic_num})")
            is_found = True

    if is_found:
        break

else:
    print(f"{combinations} combinations - neither equals {magic_num}")