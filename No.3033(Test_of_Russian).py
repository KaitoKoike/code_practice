n,m,x = map(int,input().split(" "))

liar = n-m
if x - liar >= 3:
    print("YES")
else:
    print("NO")
