from decimal import *
n = int(input())

number_list = list(int,map(input().split()))
number_list.sort()
max_number = max(number_list)
middle_number = Decimal(max_number) / Decimal(2)
for i in range(len(number_list)-1):
    if (number_list[i]-middle_number)*(number_list[i+1]-middle_number) < 0:
        if abs(number_list[i]-middle_number) <= abs(number_list[i+1]-middle_number):
            print(max_number,number_list[i])
            break
        else:
            print(max_number,number_list[i+1])
            break
    else:
        pass
