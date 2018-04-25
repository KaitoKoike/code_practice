h,w = map(int,input().split())
counter = 0
space = [[-1 for i in range(w+2)]]
for i in range(1,h+1):
    r = input()
    s = list("#"+r+"#")
    counter += r.count("#")
    space.append([])
    for j,moji in enumerate(s):
        if moji == ".":
            space[i].append(0)
        elif moji =="#":
            space[i].append(-1)
space.append([-1 for i in range(w+2)])

sx,sy = 1,1
ex,ey = h,w

watch_space = [[sx,sy]]
decided_space = [[sx,sy]]
flag = 0
while(True):
    tmp = list()
    for [i,j] in watch_space:
        if [i-1,j] not in decided_space and space[i-1][j] == 0:
            space[i-1][j] = space[i][j]+ 1
            decided_space.append([i-1,j])
            tmp.append([i-1,j])
        if [i+1,j] not in decided_space and space[i+1][j] == 0:
            space[i+1][j] = space[i][j]+ 1
            decided_space.append([i+1,j])
            tmp.append([i+1,j])
        if [i,j+1] not in decided_space and space[i][j+1] == 0:
            space[i][j+1] = space[i][j]+ 1
            decided_space.append([i,j+1])
            tmp.append([i,j+1])
        if [i,j-1] not in decided_space and space[i][j-1] == 0:
            space[i][j-1] = space[i][j]+ 1
            decided_space.append([i,j-1])
            tmp.append([i,j-1])
    watch_space = tmp
    if [ex,ey] in decided_space:
        break
    elif len(watch_space) < 1:
        flag = -1
        break
if flag == 0:
    ans = (w*h)-(space[ex][ey]+1) - counter
    print(ans)
else:
    print(-1)
