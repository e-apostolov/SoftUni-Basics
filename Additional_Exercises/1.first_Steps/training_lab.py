from math import floor

width = float(input())
height = float(input())

working_desk_width = 120
working_desk_height = 70
corridor_height = 100

remaining_height = (height * 100) - corridor_height
available_desks_height = floor(remaining_height/working_desk_height)
available_desks_width = floor((width * 100) / working_desk_width)

available_desks = (available_desks_height * available_desks_width) - 3

print(f"{available_desks:.0f}")