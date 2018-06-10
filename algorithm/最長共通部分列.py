n = int(input())

for i in range(n):
    s = list(input())
    t = list(input())
    dp = [[0 for j in range(len(s)+1)] for k in range(len(t)+1)]

    for j in range(len(s)):
        for k in range(len(t)):
            if s[j]==t[k]:
                dp[k+1][j+1] = max(dp[k][j]+1,dp[k+1][j+1])
            else:
                dp[k+1][j+1] = max(dp[k+1][j+1],dp[k+1][j])
                dp[k+1][j+1] = max(dp[k+1][j+1],dp[k][j+1])
    print(dp[len(t)][len(s)])
