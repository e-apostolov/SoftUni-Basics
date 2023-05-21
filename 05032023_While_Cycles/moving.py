width = int(input())
length = int(input())
height = int(input())

total_available_size = width * length * height

while True:
    boxes = input()
    if boxes == "Done":
        break
    boxes = int(boxes)
    total_available_size -= boxes
    if total_available_size <= 0:
        break

if total_available_size <= 0:
    print(f"No more free space! You need {abs(total_available_size)} Cubic meters more.")
else:
    print(f"{total_available_size} Cubic meters left.")

