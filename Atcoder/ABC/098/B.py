n = int(input())
s = list(input())
dp = [0 for i in range(n+1)]

for i in range(n):
    if (s[i] in s[i+1:]) and (s[i] not in s[:i]):
        dp[i+1] = dp[i]+1
    elif (s[i] not in s[i+1:]) and (s[i] in s[:i]):
        dp[i+1] = dp[i]-1
    else:
        dp[i+1] = dp[i]

print(max(dp))
