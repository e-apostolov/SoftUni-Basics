vacation_cost = float(input())
available_money = float(input())
count_spend = 0
days_passed = 0


while True:
    spend_or_save = input()
    spend_or_save_amount = float(input())
    days_passed += 1
    if spend_or_save == "spend":
        count_spend += 1
        available_money -= spend_or_save_amount
        if available_money < 0:
            available_money = 0
    elif spend_or_save == "save":
        count_spend = 0
        available_money += spend_or_save_amount
    if available_money >= vacation_cost:
        print(f"You saved the money for {days_passed} days.")
        break
    if count_spend >= 5:
        print("You can't save the money.")
        print(f"{days_passed}")
        break
