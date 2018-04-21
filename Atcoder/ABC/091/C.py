n = int(input())
red_point = {}
blue_point = {}

for i in range(n):
    red_point[list(map(int,input().split()))] = 0

for i in range(n):
    blue_point[list(map(int,input().split()))] = 0

red_point.sort(key=lambda x:x[0])
blue_point.sort(key=lambda x:x[0])
print(red_point)
print(blue_point)
counter = 0

for i in range(n)[::-1]:
    for j in range(n)[::-1]:
        if red_point[i][0] < blue_point[i][0] and red_point[i][1] < blue_point[j][0]:
            counter += 1
            break


            


print(counter)
