
hundred_yen = int(input())
twentyfive_yen = int(input())
one_yen = int(input())

twentyfive_yen += int(one_yen/25)
one_yen = one_yen%25

hundred_yen += int(twentyfive_yen/4)
twentyfive_yen = twentyfive_yen % 4

hundred_yen = hundred_yen%10

all_amount =  hundred_yen + twentyfive_yen + one_yen
print(all_amount)
