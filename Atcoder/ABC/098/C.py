n = int(input())
S = list(input())
dp = [0 for i in range(n)]
dp[0] = S[1:].count("E")

for i in range(n-1):
    if S[i] == S[i+1] == "E":
        dp[i+1] = dp[i]-1
    elif S[i] == S[i+1] == "W":
        dp[i+1] = dp[i]+ 1
    else:
        dp[i+1] = dp[i]

print(min(dp))
