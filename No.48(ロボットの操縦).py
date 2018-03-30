import math

x = int(input())
y = int(input())
l = int(input())


#y方向について
if y%l == 0 :
    y_order_times = math.fabs(int(y/l))
else:
    y_order_times = math.fabs(int(y/l)) + 1

#x方向について
if x%l == 0 :
    x_order_times = math.fabs(int(x/l))
else:
    x_order_times = math.fabs(int(x/l)) + 1

#方向転換
if y >= 0 :
    if x is not 0:
        change_direct = 1
    else:
        change_direct = 0

else:
    change_direct = 2

total_order_times = x_order_times + y_order_times + change_direct
print(int(total_order_times))
