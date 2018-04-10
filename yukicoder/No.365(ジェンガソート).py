#ブロックの数
number_block = int(input())
blocks = list(map(int,input().split()))

number_right_order = number_block

for block in blocks[::-1]:
    if number_right_order == block:
        number_right_order -= 1


print(number_right_order)
