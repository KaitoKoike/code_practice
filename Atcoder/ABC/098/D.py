
N = int(input())
numbers = list(map(int,input().split()))
ans = 0
for i in range(N):
    xor_number = 0
    sum_number = 0
    for j in range(i,N):
        sum_number += numbers[j]
        xor_number = xor_number^numbers[j]
        if sum_number == xor_number :
            ans+=1
print(ans)
