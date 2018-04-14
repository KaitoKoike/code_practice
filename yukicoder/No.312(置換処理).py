import math

number = int(input())

square_number = int(math.sqrt(number))

ans = 0

if number % 2 == 0:
    ans = int(number / 2)

for i in range(3,square_number+1):
    if number % i ==0 :
        ans = i
        break
if ans == 0 or ans == 2:
    print(number)
else:
    print(ans)
