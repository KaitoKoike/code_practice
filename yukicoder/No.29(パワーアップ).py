defeat_times = int(input())

item_list = [0 for i in range(10)]

for t in range(defeat_times):
    item_number = list(map(int,input().split(" ")))
    for i in item_number:
        item_list[i-1] += 1


powerup_counter = 0

for (i,item)in enumerate(item_list):
    if item > 1:
        powerup_counter += int(item/2)
        item_list[i] = int(item%2)


powerup_counter += int(item_list.count(1)/4)

print(powerup_counter)
