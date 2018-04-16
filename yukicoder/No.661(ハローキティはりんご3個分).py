n = int(input())

for i in range(n):
    number = int(input())
    if number % 8 == 0 and number % 10 == 0 :
        print("ikisugi")
    elif number % 8 == 0 :
        print("iki")
    elif number % 10 == 0 :
        print("sugi")
    else:
        kiti = int(number / 3)
        print(kiti)
