number_list = list(map(int,input().split()))

number_list.sort()

a = number_list[0]
b = number_list[1]
c = number_list[2]
counter = 0

if (b-a)%2==0:
    counter += (b-a)/2
    counter += (c-b)
    print(int(counter))

else:
    a = a + 1
    c = c + 1
    counter += (b-a)/2
    counter += (c-b)
    print(int(counter+1))
