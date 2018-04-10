n,k = map(int,input().split(" "))

s = input().rstrip()
number_list = [i for i in range(1,len(s)+1)]

while True:
    start_number = s.find("()")
    if number_list[start_number] == k:
        print(number_list[start_number+1])
        break
    elif number_list[start_number+1] == k:
        print(number_list[start_number])
        break
    else:
        s = s.replace("()","",1)
        del number_list[start_number:start_number+2]

    if len(number_list) == 1:
        break
