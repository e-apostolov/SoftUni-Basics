import math

start_num = int(input())
end_num = int(input())

for i in range(start_num, end_num + 1):
    current_num = i
    even_sum = 0
    odd_sum = 0
    counter = math.floor(math.log10(current_num) + 1)
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

