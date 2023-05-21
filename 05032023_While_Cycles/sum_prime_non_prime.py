sum_prime = 0
sum_non_prime = 0

while True:
    number = input()
    if number == "stop":
        break
    number = int(number)

    if number < 0:
        print("Number is negative.")
        continue

    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        sum_prime += number
    else:
        sum_non_prime += number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")


