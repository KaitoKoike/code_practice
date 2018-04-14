n = int(input())
a = [1,1,1]

N = n

if n > 1:
    for i in range(N-1):
        a.append((a[0] + a[1])%(10**9+7))
        del a[0]


    print(a[2])
else:
    print(a[2])
