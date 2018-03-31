from decimal import *

n = int(input())
z_counter=0
a = int(Decimal(n) / Decimal(3))
b = int(Decimal(n) / Decimal(5))
z_counter = a*2 + b*2
print(z_counter)
