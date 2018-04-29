import itertools
n = int(input())
comb = list(itertools.permutations(range(1,n)))
ans = 0
for list_printer in comb:
    space = [0 for i in range(n)]
    score = 0
    for printer in list_printer:
        space[printer-1] = 1
        space[printer] = 1
        score += 1
        if space.count(1) == len(space):
             break
    ans += score
print(ans)
