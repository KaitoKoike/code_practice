import math

x,y,r = map(int,input().split(" "))

#ゆきちゃんからUFOの中心までのマンハッタン距離
center_dist = abs(x)+abs(y)

#UFOの境界においてゆきちゃんから最も遠い場所

#UFO中心とゆきちゃんのなす角
theta = math.pi/4
UFO_x = r * math.cos(theta)
UFO_y = r * math.sin(theta)

#UFO外縁で最も遠い場所でのマンハッタン距離
dist = center_dist + abs(UFO_x) + abs(UFO_y)

if dist - int(dist) > 0 :
    print(int(dist) + 1)
else:
    print(int(dist))
