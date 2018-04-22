n , gram = map(int,input().split())
min_gram = 100000
sum = 0

for i in range(n):
    donatu = int(input())
    if min_gram > donatu:
        min_gram = donatu
    sum += donatu

x = (gram - sum) // min_gram
ans = n + x

print(ans)
