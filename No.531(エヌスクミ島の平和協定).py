

n,m = map(int,input().split(" "))
days_for_move = 0

if n <= m :
    days_for_move = 1
else:
    if n %2 == 0:
        if n/2 <= m :
            days_for_move = 2
        else:
            days_for_move = -1
    else :
        days_for_move = -1

print(days_for_move)
