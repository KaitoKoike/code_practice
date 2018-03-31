hamu_number = input().rstrip()

hamu_number = hamu_number.replace("hamu","1").replace("ham","0")

#print(hamu_number)

a = int(hamu_number,2)
#print(a)

b = format(a*2,"b")

b = b.replace("1","hamu").replace("0","ham")
print(b)
