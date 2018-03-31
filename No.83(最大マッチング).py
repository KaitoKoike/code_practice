n = int(input())

counter = 0

while True:
    n = n - 2
    counter += 1
    if n < 2 :
        break
if n == 0:
    print("1"*counter)
else:
    print('7'+"1"*(counter-1))
