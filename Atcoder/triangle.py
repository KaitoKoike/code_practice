import math
triangle_list = [0 for i in range(4)]
while(True):
    point = list(map(int,input().split()))
    point=sorted(point)
    z = math.sqrt(point[0]**2 + point[1]**2)

    if point[2] >= (point[1]+ point[0]):
        break
    elif point[2] < z:
        triangle_list[0] += 1
        triangle_list[2] += 1
    elif point[2] == z:
        triangle_list[0]+= 1
        triangle_list[1]+= 1
    elif point[2] > z:
        triangle_list[0] += 1
        triangle_list[3] += 1

print("{0[0]} {0[1]} {0[2]} {0[3]}".format(triangle_list))
