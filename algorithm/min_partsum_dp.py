N = int(input())
a = list(map(int,input().split()))
A = int(input())

dp = [[987654321 for j in range(A+1)]for i in range(N+1)]
dp[0][0] = 0
#動的計画法
for i in range(N):
    for j in range(A+1):
        if j - a[i] >= 0:
            dp[i+1][j] = min(dp[i][j-a[i]]+1,dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]
print(dp)
