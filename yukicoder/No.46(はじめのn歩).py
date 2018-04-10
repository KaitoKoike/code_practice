list_setting = list(map(int,input().split(" ")))
a = list_setting[0]
b = list_setting[1]

number_of_walk = b / a

if number_of_walk > int(number_of_walk):
    print(int(number_of_walk)+1)
else:
    print(int(number_of_walk))
