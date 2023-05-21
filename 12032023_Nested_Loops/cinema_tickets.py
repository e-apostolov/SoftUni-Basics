student_tickets = 0
standard_tickets = 0
kids_tickets = 0


while True:
    movie = input()
    if movie == "Finish":
        break
    available_seats = int(input())
    taken_seats = 0
    while available_seats > taken_seats:
        ticket_type = input()
        if ticket_type == "End":
            break
        taken_seats += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
    print(f"{movie} - {(taken_seats / available_seats) * 100:.2f}% full.")

total_tickets = standard_tickets + student_tickets + kids_tickets

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets) * 100:.2f}% kids tickets.")