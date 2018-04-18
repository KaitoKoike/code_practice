import unicodedata

n = int(input())

s = ord("A")

counter = []


ans = ""
while (n >= 0):
    n,m = divmod(n,26)
    ans = chr( s + m) + ans
    n -= 1

print(ans)
