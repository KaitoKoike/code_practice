#ブロックの数
number_block = int(input())
blocks = list(map(int,input().split()))

max_length = 0
move_index = 0

for block in blocks:
    if block > max_length:
        max_length = block
    else:
        move_index = max(move_index,block)

ans = 0

for block in blocks:
    if block <= move_index:
        ans += 1
print(ans)
