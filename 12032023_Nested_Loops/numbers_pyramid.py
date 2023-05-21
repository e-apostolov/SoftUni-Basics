n = int(input())
current_num = 1
is_bigger_n = False

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if current_num > n:
            is_bigger_n = True
            break
        print(current_num, end=" ")
        current_num += 1

    if is_bigger_n:
        break

    print()