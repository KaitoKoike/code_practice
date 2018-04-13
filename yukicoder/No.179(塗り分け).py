h,w = map(int,input().split(" "))
space = [[0 for j in range(w)] for i in range(h)]

for i in range(h):
    tmp = list(input())
    for j in range(w):
        if tmp[j] == "#":
            space[i][j] = 0
        else :
            space[i][j] = -1

dm1_space = [flatten for inner in space for flatten in inner]

if 0 not in dm1_space :
    print("No")
    exit()
for move in range(1,len(dm1_space)):
    space_dummy = dm1_space[:]
    print(move)
    d = -1
    for point in range(len(space_dummy)):

        if space_dummy[point] == 0 :
            if point + move < len(space_dummy) and space_dummy[point+move] == 0 and (d==(point+move)//w- (point)//w or d == -1):
                space_dummy[point+move] = -1
                space_dummy[point] = -1
                d = (move+point)//w - (point)//w

            else:
                break

    else:
        print("Yes")
        break
else :
    print("No")
