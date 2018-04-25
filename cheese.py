h,w,n = map(int,input().split())

space = [[-1 for i in range(w+2)]]
factory = {}
for i in range(1,h+1):
    space.append([])
    s = ["X"]+list(input())+["X"]
    for l,j in enumerate(s):
        if j == ".":
            space[i].append(0)
        elif j =="X":
            space[i].append(-1)
        elif j =="S":
            space[i].append(0)
            factory[0] = [i,l]
        else:
            number = int(j)
            space[i].append(0)
            factory[number] = [i,l]
space.append([-1 for i in range(w+2)])
space_tmp = [x[:] for x in space]

ans = 0
for i in factory.keys():
    space = [x[:] for x in space_tmp]
    if i+1 in factory.keys():
        [ex,ey]= factory[i+1]
        decided_space = [factory[i]]
        watch_space = [factory[i]]
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
        ans += space[ex][ey]
print(ans)
