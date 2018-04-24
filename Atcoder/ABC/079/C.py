s = input()

for i in range(1<<len(s)-1):
    t = list(s)
    for j in reversed(range(1,len(s))):
        if i & (1<<(j-1)):
            t = t[:j]+["+"]+t[j:]
        else:
            t = t[:j]+["-"]+t[j:]
    ans = eval("".join(t))
    if ans == 7:
        break

print("".join(t)+"=7")
