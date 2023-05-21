number_of_groups = int(input())
total_climbers = 0

count_group_musala = 0
count_group_monblan = 0
count_group_kilimanjaro = 0
count_group_k2 = 0
count_group_everest = 0

for i in range(number_of_groups):
    number_of_climbers = int(input())
    total_climbers += number_of_climbers
    if number_of_climbers <= 5:
        count_group_musala += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        count_group_monblan += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        count_group_kilimanjaro += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        count_group_k2 += number_of_climbers
    else:
        count_group_everest += number_of_climbers

print(f"{count_group_musala / total_climbers * 100:.2f}%")
print(f"{count_group_monblan / total_climbers * 100:.2f}%")
print(f"{count_group_kilimanjaro / total_climbers * 100:.2f}%")
print(f"{count_group_k2 / total_climbers* 100:.2f}%")
print(f"{count_group_everest / total_climbers* 100:.2f}%")




