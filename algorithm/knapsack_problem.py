N,W = map(int,input().split())
dp = [[0 for i in range(W+1)]for j in range(N+1)]
v_list = []
w_list = []
for i in range(N):
    v,w = map(int,input().split())
    v_list.append(v)
    w_list.append(w)


for i in range(N):
    for j in range(W+1):
        if j - w_list[i] >= 0:
            dp[i+1][j] = max(dp[i+1][j-w_list[i]]+v_list[i],dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[N][W])
