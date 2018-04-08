a , b, k = map(int,input().split())

if (b-a) > k:
    small_list = [i for i in range(a,a+k)]

    big_list = [j for j in range(b-k+1,b+1)]

    for number in small_list:
        if number in big_list:
            small_list.remove(number)

    list_number = small_list + big_list

else:
    list_number = range(a,b+1)

for i in list_number:
    print(i)
