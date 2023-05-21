import string

alphabet = string.ascii_lowercase

for i in range (0, len(alphabet)):
    for j in range (0, len(alphabet)):
        for k in range (0, len(alphabet)):
            for l in range(0, len(alphabet)):
                print(f"{alphabet[i]}{alphabet[j]}{alphabet[k]}{alphabet[l]}")

                