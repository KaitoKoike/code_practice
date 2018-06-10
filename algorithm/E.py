Y ,W = map(int,input().split())
N,M,D = map(int,input().split())
stick_holy = []

for n in range(N):
    stick_holy.append(int(input()))
BC_list = []
for i in range(M):
    BC_list.append(list(map(int,input().split())))

for d in range(1,W+1):
    holyday = stick_holy[:]
    for b,c in BC_list:
        if c >= d:
            holyday.append((c-d)+(b-1)*W+1)
        else:
            holyday.append((c-d)+b*W+1)
    holyday_add = []
    holyday = sorted(holyday)
    for i in range(len(holyday)):
        for j in range(len(holyday)):
            if holyday[j]-holyday[i] -1 > D:
                break
            else:
                holyday_add += range(holyday[i]+1,holyday[j])
    holyday_add =  set(holyday_add)
    holyday = set(holyday)
    print(len(holyday|holyday_add))
