n = int(input())
point_list = list(map(int,input().split()))
score_list = []
dp = [0 for i in range(int(1e+4)+1)]
dp[0] = 1

for i in range(1<<n):
    get_score = 0
    for j in reversed(range(n)):
        if i&(1<<j):
            get_score+=point_list[j]
    if get_score not in score_list:
        score_list.append(get_score)

print(len(score_list))
