name_of_player = input()
max_goals = 0
scorer_name = ""

while name_of_player != "END":
    scored_goals = int(input())
    if scored_goals > max_goals:
        scorer_name = name_of_player
        max_goals = scored_goals
        if scored_goals >= 10:
            break
    name_of_player = input()

print(f"{scorer_name} is the best player!")

if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")






