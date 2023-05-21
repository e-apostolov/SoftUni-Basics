start_range = int(input())
end_range = int(input())
magic_number = int(input())
count = 0
success = 0

for i in range(start_range, end_range + 1):
    for j in range(start_range, end_range + 1):
        count += 1
        if i + j == magic_number:
            success += 1
            if success == 1:
                print(f"Combination N:{count} ({i} + {j} = {magic_number})")
                break


if success == 0:
    print(f"{count} combinations - neither equals {magic_number}")



