position_of_cup = int(input())
change_times = int(input())

for i in range(change_times):
    change_position = list(map(int,input().split(" ")))
    if position_of_cup in change_position:
        if position_of_cup == change_position[0]:
            position_of_cup = change_position[1]
        else:
            position_of_cup = change_position[0]

print(position_of_cup)
