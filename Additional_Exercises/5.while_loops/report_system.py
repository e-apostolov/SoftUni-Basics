target_sum = int(input())
installment = 0
cash_payment = 0
card_payment = 0
cash_payment_total = 0
card_payment_total = 0

while target_sum > 0:
    price = input()
    if price == "End":
        print("Failed to collect required money for charity.")
        break
    price = int(price)
    installment += 1
    if (installment % 2 != 0 and price <= 100) or (installment % 2 == 0 and price > 10):
        print("Product sold!")
        target_sum -= price

        if installment % 2 != 0:
            cash_payment_total += price
            cash_payment += 1
        else:
            card_payment_total += price
            card_payment += 1

    else:
        print("Error in transaction!")

else:
    print(f"Average CS: {cash_payment_total / cash_payment:.2f}")
    print(f"Average CC: {card_payment_total / card_payment:.2f}")





