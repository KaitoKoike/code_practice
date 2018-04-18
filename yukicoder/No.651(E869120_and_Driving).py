from decimal import *

a = int(input())

h = 10
m = 0

hour =  h + a // 100
minuite = "%02d" % int((Decimal(a) / Decimal(100) - Decimal(a) // Decimal(100)) * Decimal(60))
print("{}:{}".format(hour,minuite))
