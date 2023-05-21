start_number = int(input())
end_number = int(input())

for i in range(start_number, end_number + 1):
    even_sum = 0
    odd_sum = 0
    current_num = i
    counter = len(str(current_num))
    while counter > 0:
        digit = current_num % 10
        if counter % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        current_num = current_num // 10
        counter -= 1

    if even_sum == odd_sum:
        print(i, end=" ")

