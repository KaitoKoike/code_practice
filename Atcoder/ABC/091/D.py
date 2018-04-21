n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

c_list = []

for i in range(n):
    for j in range(n):
        c_list.append(a_list[i]+b_list[j])



max_len = len(bin(max(c_list))) -2
ans_list = [0 for i in range(max_len)]

for number in c_list:
    bin_number = list(bin(number).replace("0b",""))
    if len(bin_number) < max_len:
        add_zero = ["0" for i in range((max_len-len(bin_number)))]
        bin_number = add_zero + bin_number
    for i in range(len(bin_number)):
        ans_list[i] += int(bin_number[i])

for i in range(len(ans_list)):
    if ans_list[i] % 2 == 0:
        ans_list[i] = 0
    else:
        ans_list[i] = 1
ans = ""

for i in ans_list:
    ans = ans + str(i)

print(int(ans,2))
