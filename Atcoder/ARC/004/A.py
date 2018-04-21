import math

n = int(input())
point_list = []
for i in range(n):
    point = list(map(int,input().split()))
    point_list.append(point)

max_dist = 0

for point_a in point_list:
    for point_b in point_list:
        dist = math.sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2)
        if dist > max_dist:
            max_dist = dist
print(max_dist)
