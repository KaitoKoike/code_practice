A , B ,N = map(int,input().split())
x = list(input())

for cons in x:
    if cons == "S":
        if A > 0:
            A -= 1
    elif cons == "C":
        if B >0:
            B -= 1
    else:
        if A > 0 and  B > 0:
            if A >= B :
                A -= 1
            else :
                B -= 1
        elif A > 0 and B == 0:
            A -= 1
        elif B > 0 and A == 0:
            B -= 1
        else:
            pass
print(A)
print(B)
