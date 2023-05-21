non_working_days = int(input())

working_days = 365 - non_working_days
needed_time_to_sleep = 30000

working_days_play = 63
non_working_days_play = 127

total_time_to_play = (working_days_play * working_days) + (non_working_days_play * non_working_days)
diff = abs(needed_time_to_sleep - total_time_to_play)

diff_default = diff / 60
diff_in_hours = diff // 60
diff_in_minutes = diff % 60


if total_time_to_play >= needed_time_to_sleep:
    print("Tom will run away")
    print(f"{diff_in_hours} hours and {diff_in_minutes} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{diff_in_hours} hours and {diff_in_minutes} minutes less for play")
