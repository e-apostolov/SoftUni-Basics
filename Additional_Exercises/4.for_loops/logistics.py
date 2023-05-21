count_of_freight = int(input())

count_microbus = 0
transported_microbus = 0
count_truck = 0
transported_truck = 0
count_train = 0
transported_train = 0
cost = 0
total_weight = 0

for i in range(count_of_freight):
    weight_of_freight = int(input())
    if weight_of_freight <= 3:
        count_microbus += 1
        transported_microbus += weight_of_freight
        cost += weight_of_freight * 200
    elif 4 <= weight_of_freight <= 11:
        count_truck += 1
        transported_truck += weight_of_freight
        cost += weight_of_freight * 175
    else:
        count_train += 1
        transported_train += weight_of_freight
        cost += weight_of_freight * 120

total_transported = transported_microbus + transported_truck + transported_train

print(f"{cost / total_transported:.2f}")
print(f"{transported_microbus / total_transported * 100:.2f}%")
print(f"{transported_truck / total_transported * 100:.2f}%")
print(f"{transported_train / total_transported * 100:.2f}%")