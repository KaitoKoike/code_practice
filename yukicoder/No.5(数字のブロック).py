"""
入力
L,
N,
W1,W2,W3...
"""

max = int(input())
n = int(input())
list_of_block = list(map(int,input().split()))
box_rest = max
counter = 0


for i in range(n):
    w = int(min(list_of_block))
    list_of_block.remove(w)
    box_rest = box_rest - w
    if box_rest < 0:
        break
    else:
        counter += 1
        pass

print(counter)
