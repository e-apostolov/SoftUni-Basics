letter_1 = input()
letter_2 = input()
letter_3 = input()
combinations = 0

for i in range(ord(letter_1), ord(letter_2) + 1):
    if i != ord(letter_3):
        for j in range(ord(letter_1), ord(letter_2) +1):
            if j != ord(letter_3):
                for k in range(ord(letter_1), ord(letter_2) + 1):
                    if k != ord(letter_3):
                        combinations += 1
                        print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")

print(combinations)
