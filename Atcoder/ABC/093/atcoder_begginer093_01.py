s = input()
s = s.replace("a","",1)
s = s.replace("b","",1)
s = s.replace("c","",1)

if bool(s) is not True:
    print("Yes")
else:
    print("No")
