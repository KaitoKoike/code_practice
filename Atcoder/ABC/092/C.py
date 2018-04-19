
n = int(input())
spot_list = list(map(int,input().split()))
max_cost = 0

#maxの計算
for i in range(1,len(spot_list)):
    max_cost += abs(spot_list[i]-spot_list[i-1])
max_cost += abs(spot_list[0])+abs(spot_list[len(spot_list)-1])

spot_list = [0] + spot_list + [0]
for i in range(1,len(spot_list)-1):
    d_pay = abs(spot_list[i-1]-spot_list[i+1]) - (abs(spot_list[i]-spot_list[i-1])+abs(spot_list[i+1]-spot_list[i]))
    print(max_cost+d_pay)
