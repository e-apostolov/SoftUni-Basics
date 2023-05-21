month = input()
no_of_nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50 * no_of_nights
    apartment_price = 65 * no_of_nights
elif month == "June" or month == "September":
    studio_price = 75.20 * no_of_nights
    apartment_price = 68.70 * no_of_nights
elif month == "July" or month == "August":
    studio_price = 76 * no_of_nights
    apartment_price = 77 * no_of_nights


if 14 > no_of_nights > 7 and (month == "May" or month == "October"):
    studio_price -= studio_price * 0.05
elif no_of_nights > 14 and (month == "May" or month == "October"):
    studio_price -= studio_price * 0.30
elif no_of_nights > 14 and (month == "June" or month == "September"):
    studio_price -= studio_price * 0.20
if no_of_nights > 14:
    apartment_price -= apartment_price * 0.10

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")