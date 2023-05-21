movie_name = input()
hall = input()
tickets = int(input())
ticket_price = 0

if movie_name == "A Star Is Born":
    if hall == "normal":
        ticket_price = 7.5
    elif hall == "luxury":
        ticket_price = 10.5
    elif hall == "ultra luxury":
        ticket_price = 13.5
elif movie_name == "Bohemian Rhapsody":
    if hall == "normal":
        ticket_price = 7.35
    elif hall == "luxury":
        ticket_price = 9.45
    elif hall == "ultra luxury":
        ticket_price = 12.75
elif movie_name == "Green Book":
    if hall == "normal":
        ticket_price = 8.15
    elif hall == "luxury":
        ticket_price = 10.25
    elif hall == "ultra luxury":
        ticket_price = 13.25
elif movie_name == "The Favourite":
    if hall == "normal":
        ticket_price = 8.75
    elif hall == "luxury":
        ticket_price = 11.55
    elif hall == "ultra luxury":
        ticket_price = 13.95

print(f"{movie_name} -> {tickets * ticket_price:.2f} lv.")