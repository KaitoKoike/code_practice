s=input()
ret=0
# ループを各文字の間bit分回す
for i in range(1<<(len(s)-1)):
    t=list(s)
    # 実はiとjの向きについてあまり深く考える必要は無いです。どうせ全探索するので。
    for j in reversed(range(1, len(s))):
        if i&(1<<(j-1)):
            t=t[:j]+["+"]+t[j:]
            print(t)
    ret+=eval("".join(t))
    print(ret)
