from decimal import *
import math

n = int(input())

r = math.sqrt(Decimal(n) / Decimal(3) )

if r > 1:
    r = int(r)
else:
    r = 1

print(r)
