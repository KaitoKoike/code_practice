
n = int(input())
a = 1
counter = 0

while True:
    a = a * 2
    if a > n:
        a = a/2
        break
    counter += 1

b = n - a

if b == 0:
    print(counter)

else :
    print(counter+1)
