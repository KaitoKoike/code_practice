N = int(input())

a = list(map(int,input().split()))
A = int(input())
dp = [[0 for i in range(N+1)] for j in range(A+1)]
dp[0][0] = 1

for j in range(A+1):
    for i in range(N):
        if j-a[i] >= 0:
            dp[j][i+1] = dp[j-a[i]][i] or dp[j][i]
        else:
            dp[j][i+1] = dp[j][i]
print(dp)
