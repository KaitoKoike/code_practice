n,m = map(int,input().split())

S = list(input())
T = list(input())

dp = [[987654321 for i in range(len(S)+1)] for j in range(len(T)+1)]
dp[0][0] = 0

"""
#変更
if S[i] == T[j]:
    dp[j+1][i+1] = dp[j][i]
else:
    dp[j+1][i+1] = dp[j][i] + 1

#削除
dp[j+1][i+1] = dp[j+1][i] + 1

#挿入
dp[j+1][i+1] = dp[j][i+1] + 1
"""

for i in range(-1,len(S)):
    for j in range(-1,len(T)):
        if i >=0 and j >= 0:
            if S[i]== T[j]:
                dp[j+1][i+1] = min(dp[j][i],dp[j+1][i+1])
            else:
                dp[j+1][i+1] = min(dp[j][i]+1,dp[j+1][i+1])
        if i >= 0:
            dp[j+1][i+1] = min(dp[j+1][i]+1,dp[j+1][i+1])
        if j >= 0:
            dp[j+1][i+1] = min(dp[j][i+1]+1,dp[j+1][i+1])

print(dp[len(T)][len(S)])
#[len(T)][len(S)]
