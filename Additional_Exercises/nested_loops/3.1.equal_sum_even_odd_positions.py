first_number = int(input())
second_number = int(input())

for a in range(first_number, second_number + 1):
    current_num_str = str(a)
    sum_even = 0
    sum_odd = 0
    for symbol_count in range(0, len(current_num_str)):
        digit = int(current_num_str[symbol_count])
        if symbol_count % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
    if sum_even == sum_odd:
        print(current_num_str, end=" ")

