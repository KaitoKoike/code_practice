n,y = map(int,input().split())
ans = None

for a in range((y//10000)+1):
    for b in range((y//5000)+1):
        c = n - (a+b)
        if c < 0:
            break
        elif y == 10000*a + 5000*b + 1000*c:
            ans = [a,b,c]
    if ans is not None:
        break

if ans is not None:
    print(ans[0],ans[1],ans[2])
else:
    print("-1 -1 -1")
