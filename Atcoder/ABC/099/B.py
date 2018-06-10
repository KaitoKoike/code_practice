a,b = map(int,input().split())

n = abs(a-b)
tree_1 = 0
tree_2 = 0
for i in range(1,n):
    tree_1 += i
for i in range(1,n+1):
    tree_2 += i

print(tree_1 - a)
