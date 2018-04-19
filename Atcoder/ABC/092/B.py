n = int(input())
d,x = map(int,input().split())
all_choco = 0

for person in range(n):
    day = int(input())
    choco_for_person = (d-1)//day + 1
    all_choco += choco_for_person

print(all_choco+x)
