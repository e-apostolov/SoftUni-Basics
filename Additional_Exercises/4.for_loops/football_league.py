stadium_capacity = int(input())
fans_num = int(input())
sector_A_fans = 0
sector_B_fans = 0
sector_V_fans = 0
sector_G_fans = 0


for i in range(fans_num):
    sector = input()
    if sector == "A":
        sector_A_fans += 1
    elif sector == "B":
        sector_B_fans += 1
    elif sector == "V":
        sector_V_fans += 1
    elif sector == "G":
        sector_G_fans += 1

total_fans = sector_A_fans + sector_B_fans + sector_V_fans + sector_G_fans

print(f"{sector_A_fans / total_fans * 100:.2f}%")
print(f"{sector_B_fans / total_fans * 100:.2f}%")
print(f"{sector_V_fans / total_fans * 100:.2f}%")
print(f"{sector_G_fans / total_fans * 100:.2f}%")
print(f"{fans_num / stadium_capacity * 100:.2f}%")