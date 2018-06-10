a = int(input())
b = int(input())
max_num = 0

for i in range(101)[::-1]:
    if i <= a and i % b == 0:
        max_num = max(i,max_num)
        break

print(max_num)
