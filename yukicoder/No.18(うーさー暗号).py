
angou = list(input())
hira = []
n = len(angou)

for i in range(n):
    moji = chr(ord("Z") - (ord("Z") - ord(angou[i]) + (i+1)) % 26 )
    hira.append(moji)
hirabun = "".join(hira)
print(hirabun)
