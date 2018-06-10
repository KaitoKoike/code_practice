N = int(input())
a = list(map(int,input().split()))
A = int(input())

#aの中にある数字からAになるように数字を選ぶ方法は何通りあるか
dp = [[0 for i in range(N+1)] for j in range(A+1)]
dp[0][0] = 1

for j in range(A+1):
    for i in range(N):
        if j-a[i] >= 0:
            dp[j][i+1] = dp[j-a[i]][i] + dp[j][i]
        else:
            dp[j][i+1] = dp[j][i]

print(dp)
