import time
start = time.time()
n = int(input())
max = 100000
dp = [max for i in range(n+1)]
dp[0] = 0
div_list = [1]
j = 1
k = 1
while(j*6 <= n):
    if 6**j <= n:
        if 6**j not in div_list:
            div_list.append(6**j)
    if 9**k <= n:
        if 9**k not in div_list:
            div_list.append(9**j)
    if 6**k > n and 9**j > n:
        break
    j += 1
    k+= 1
sorted(div_list)

for i in range(n):
    for n in div_list:
        dp[n] = 1
        if i+1-n > 0:
            dp[i+1] = min(dp[i+1],dp[i+1-n]+1)
        else:
            break

print(dp[len(dp)-1])
print(time.time()-start)
