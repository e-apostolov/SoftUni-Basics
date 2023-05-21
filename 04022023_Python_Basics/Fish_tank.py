aquarium_length = int(input())
aquarium_width = int(input())
aquarium_height = int(input())
misc_percentage = float(input())

aquarium_capacity_sm2 = aquarium_length * aquarium_width * aquarium_height
aquarium_capacity_liters = aquarium_capacity_sm2 / 1000
used_capacity = misc_percentage / 100

aquarium_capacity_liters = aquarium_capacity_liters - (aquarium_capacity_liters * used_capacity)
print(aquarium_capacity_liters)




