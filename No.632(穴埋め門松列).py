a = input().split(" ")

judge = {"1":0,"4":0}

for i in range(len(a)):
    if a[i] == "?":
        a[i] = "1"
        b = int(a[1]) - int(a[0])
        c = int(a[1]) - int(a[2])
        if b*c > 0:
            judge["1"] = 1

        a[i] = "4"
        b = int(a[1]) - int(a[0])
        c = int(a[1]) - int(a[2])
        if b*c > 0:
            judge["4"] = 1

if judge["1"] == 1 and judge["4"] == 1:
    print(14)
elif judge["1"] == 1 :
    print(1)
elif judge["4"] == 1 :
    print(4)
