r,c = map(int,input().split())
sx,sy = map(int,input().split())
ex,ey = map(int,input().split())
space_list = list()
space = list()
for i in range(r):
    space.append([])
    s = list(input())
    for n,j in enumerate(s):
        if j == "#":
            space[i].append(-1)
        else:
            space[i].append(0)
            space_list.append([i,n])
decided_space = [[sx-1,sy-1]]
watch_space = [[sx-1,sy-1]]
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
    if [ex-1,ey-1] in decided_space:
        break
print(space[ex-1][ey-1])
