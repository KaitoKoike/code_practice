from decimal import *
a,b = map(int,input().split(" "))

payment = Decimal(a) * (Decimal(1) + Decimal(b)/Decimal(100) )
print(int(payment))
