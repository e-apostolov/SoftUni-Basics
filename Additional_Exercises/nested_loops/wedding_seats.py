last_sector = input()
first_row_seats = int(input())
seats_uneven_row = int(input())
n = 0
total_seats = 0

for sectors in range(ord("A"), ord(last_sector) + 1):
    n += 1
    for rows in range(1, first_row_seats + n):
        if rows % 2 != 0:
            for seats in range(1, seats_uneven_row + 1):
                seats = chr(seats + 96)
                print(f"{chr(sectors)}{rows}{seats}")
                total_seats += 1
        else:
            for seats in range(1, seats_uneven_row + 3):
                seats = chr(seats + 96)
                print(f"{chr(sectors)}{rows}{seats}")
                total_seats += 1

print(total_seats)
