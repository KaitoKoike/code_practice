input = input().split()
N = int(input[0])
p = float(input[1])

a = [0 for i in range(N+1)]

for i in range(2,N+1):
    for j in range(i*2,N+1,i):
        a[j] += 1
del a[:2]
e = 0
for number in a:
    if number == 0 :
        e += 1
    else:
        e += (1-p)**number

print(e)
