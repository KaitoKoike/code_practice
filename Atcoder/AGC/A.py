n = int(input())
number_list = list(map(int,input().split()))
counter = 0
if n == 1:
    if number_list[0] == 0:
        print(1)
    else:
        print(0)
else:
    sum_list = number_list[:]
    for j in range(1,n):
        tmp = []
        for i in range(len(sum_list)):
            if i+j < n:
                tmp.append(sum_list[i]+number_list[i+j])
        sum_list = tmp[:]
        counter += sum_list.count(0)
print(counter)
