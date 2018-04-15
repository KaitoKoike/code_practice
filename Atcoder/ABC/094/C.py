

n = int(input())

number_list = list(map(int,input().split()))
tmp_list = sorted(number_list)


for number in number_list:
    if number < tmp_list[n//2]:
        print(tmp_list[n//2])
    else :
        print(tmp_list[n//2-1])
