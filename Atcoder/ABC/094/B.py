n ,m,x = map(int,input().split())
fee_list = list(map(int,input().split()))

pay_list= [0,0]

for i in range(x,n+1):
    if i in fee_list:
        pay_list[0] += 1

for j in range(x):
    if j in fee_list:
        pay_list[1] += 1

if pay_list[0] < pay_list[1]:
    print(pay_list[0])
else:
    print(pay_list[1])
