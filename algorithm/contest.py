n = int(input())
point_list = list(map(int,input().split()))
max_score = sum(point_list)
dp = [[0 for j in range(max_score+1)]for i in range(n+1)]
dp[0][0] = 1

for j in range(max_score+1):
    for i in range(n):
        if j - point_list[i] >= 0 :
            dp[i+1][j]= dp[i][j-point_list[i]]+dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

ans = len(dp[n])-dp[n].count(0)
print(ans)
