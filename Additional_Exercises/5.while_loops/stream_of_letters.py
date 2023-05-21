c = 0
o = 0
n = 0
sentence = ""

while True:
    letter = input()
    if letter == "End":
        break

    if letter == "c" and c == 0:
        c += 1
        letter = ""
    elif letter == "o" and o == 0:
        o += 1
        letter = ""
    elif letter == "n" and n == 0:
        n += 1
        letter = ""
    else:
        if letter.isalpha():
            sentence += letter

    if c == 1 and o == 1 and n == 1:
        c = 0
        o = 0
        n = 0
        print(sentence, end=" ")
        sentence = ""
