hour = int(input())
weekday = input()

if hour >= 10 and hour <= 18 and weekday != "Sunday":
    print('open')
else:
    print('closed')
