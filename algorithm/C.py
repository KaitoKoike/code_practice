N , D = map(int,input().split())
x = list(map(int,input().split()))
ans = []
#dp = [[[0 for k in range(N)]for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(i):
        if abs(x[i] -x[j]) <= D:
            for k in range(j):
                if abs(x[j]-x[k]) <= D and abs(x[i]-x[k]) > D:
                    ans.append([i+1,j+1,k+1])
print(len(ans))
