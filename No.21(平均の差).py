#数字の数
N = int(input())

#グループ数
K = int(input())

#数字の格納
fig = []
for i in range(N):
    fig.append(int(input()))

#最大と最小の差分
sub = max(fig) - min(fig)
print(sub)
