h,w = map(int,input().split())
space = []
for i in range(h):
    space.append([])
    s = list(input())
    print(s)
    for x in s:
        space[i].append(x)

i ,j = 0,0
dir = [0,1]
counter = 0
while(True):
    if space[i][j] == "_":
        i += dir[0]
        j += dir[1]
        counter += 1
    elif space[i][j] == "/":
        tmp = dir[0]
        dir[0] = -dir[1]
        dir[1] = -tmp
        i += dir[0]
        j += dir[1]
        counter += 1
    elif space[i][j] == "\\":
        tmp = dir[0]
        dir[0] = dir[1]
        dir[1] = tmp
        i += dir[0]
        j += dir[1]
        counter += 1
    if i < 0 or i >= h or j < 0 or j >= w:
        break
print(counter)
