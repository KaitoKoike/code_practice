n = int(input())

for i in range(n):
    a,b = map(int,input().split(" "))
    c = int(a/b)
    d = int(b/a)

    if c == 1 :
        print("=")
    elif c == 0:
        print("<")
    elif d == 0:
        print(">")
