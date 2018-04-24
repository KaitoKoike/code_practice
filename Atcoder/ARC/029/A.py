n = int(input())
meat_list = []

for i in range(n):
    meat_list.append(int(input()))

ans_minuite = float("inf")
dif_meat = float("inf")

for i in range(1<<(len(meat_list)-1)):
    meat_time_1 = 0
    meat_time_2 = 0
    for j in reversed(range(len(meat_list))):
        if i & (1<<j):
            meat_time_1 += meat_list[j]
        else :
            meat_time_2 += meat_list[j]

    if abs(meat_time_1 - meat_time_2) < dif_meat:
        dif_meat = abs(meat_time_1-meat_time_2)
        ans_minuite = max(meat_time_1,meat_time_2)

print(ans_minuite)
