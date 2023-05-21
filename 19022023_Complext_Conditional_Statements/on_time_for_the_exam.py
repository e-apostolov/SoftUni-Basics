exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_hour_in_minutes = exam_hour * 60
arrival_hour_in_minutes = arrival_hour * 60

exam_total_minutes = exam_hour_in_minutes + exam_min
arrival_total_minutes = arrival_hour_in_minutes + arrival_min

diff = abs(arrival_total_minutes - exam_total_minutes)

if arrival_total_minutes > exam_total_minutes:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours} : 0{minutes} hours after the start")
        else:
            print(f"{hours} : {minutes} hours after the start")
elif arrival_total_minutes == exam_total_minutes or diff <= 30:
    print("On time")
    if 1 <= diff <= 30:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours} : 0{minutes} hours before the start")
        else:
            print(f"{hours} : {minutes} hours before the start")