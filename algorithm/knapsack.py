N,W = map(int,input().split())
value_list = []
weight_list = []

for i in range(N):
    v,w = map(int,input().split())
    value_list.append(v)
    weight_list.append(w)

dp = [[0 for i in range(N+1)]for j in range(W+1)]
dp[W-1][0] = 0

for weight in range(W+1):
    for i in range(N):
        if weight-weight_list[i] >= 0:
            dp[weight][i+1] = max(dp[weight-weight_list[i]][i]+value_list[i],dp[weight][i])
        else:
            dp[weight][i+1] = dp[weight][i]

print(dp)
