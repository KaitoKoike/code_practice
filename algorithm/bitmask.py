#ある数値の組が渡された時にその中から数値選んで最大の総和を求める

n = int(input())
a = list(map(int,input().split()))
dp = [0 for i in range(n+1)]

for i in range(n):
    dp[i+1] = max(dp[i]+a[i],dp[i])

print(dp[n])
