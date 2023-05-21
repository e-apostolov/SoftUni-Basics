target_result = int(input())
tries = 0
current_target = target_result - 30
total_tries = 0

while True:
    current_jump = int(input())
    if current_jump > current_target:
        tries = 0
        current_target += 5
    else:
        tries += 1
    total_tries += 1
    if tries >= 3:
        print(f"Tihomir failed at {current_target}cm after {total_tries} jumps.")
        break
    if current_jump > target_result and current_target > target_result:
        print(f"Tihomir succeeded, he jumped over {target_result}cm after {total_tries} jumps.")
        break
