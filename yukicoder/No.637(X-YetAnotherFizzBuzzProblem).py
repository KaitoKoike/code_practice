a = input().split(" ")
counter = 0

for i in a :
    if int(i) % 3 == 0:
        if int(i) % 5 == 0 :
            counter += 8
        else:
            counter += 4
    elif int(i) % 5 == 0 :
        counter += 4
    else:
        counter += len(str(i))
print(counter)
