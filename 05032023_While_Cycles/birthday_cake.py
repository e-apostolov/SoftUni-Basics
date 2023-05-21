cake_width = int(input())
cake_height = int(input())
total_cake_size = cake_height * cake_width


while True:
    taking = input()
    if taking == "STOP":
        break
    taking = int(taking)
    total_cake_size -= taking
    if total_cake_size <= 0:
        break


if total_cake_size <= 0:
    print(f"No more cake left! You need {abs(total_cake_size)} pieces more.")
else:
    print(f"{total_cake_size} pieces are left.")