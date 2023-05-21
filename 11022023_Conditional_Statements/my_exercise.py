import time

first_name = input("First Name: ")
last_name = input("Last Name: ")
age = int(input("Age: "))
sex = input("Sex: ")

if sex == "Male":
    print(f"Hello Mr. {first_name}  {last_name}!")
else:
    print(f"Hello Ms. {first_name}  {last_name}!")


time.sleep(1)
print("loading...")
time.sleep(1)
print("loading...")
time.sleep(2)
print("Welcome to the first custom made program. Let it be a good journey and successful career!")
time.sleep(3)
print ("Please create an account...")

time.sleep(1)
username = input("username: ")
password = input("password: ")

time.sleep(1)
print("loading...")
time.sleep(1)
print("loading...")
time.sleep(2)

verify_password = input("Please verify your password: ")

time.sleep(2)

if verify_password == password:
    print(f"Yor account has been successfully verified, {first_name}!")
else:
    print(f"Wrong password!")

time.sleep(3)

print("Let's calculate how much your trip will cost...")

time.sleep(3)

fuel_consumption = float(input("Enter average fuel consumption: "))
trip_length = int(input("What is the length of the trip: "))
current_fuel_price = float(input("Fuel cost: "))

time.sleep(1)
print("Calculating....")
total_fuel_cost = (trip_length / fuel_consumption) * current_fuel_price
time.sleep(2)

print(f"Your trip will cost {total_fuel_cost:.2f} bgn")

time.sleep(2)
print("Bye bye....")





