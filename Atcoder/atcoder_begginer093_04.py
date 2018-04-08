n = int(input().rstrip())

for i in range(n):
    a,b = map(int,input().split())
    counter = 0
    max_score = a*b
    a_list = [i for i in range(1,max_score+1)]
    b_list = [j for j in range(1,max_score+1)]
    answer_list = []
    a_list.remove(a)
    a_list.sort(reverse=True)
    b_list.remove(b)

    for b_number in b_list[:]:
        for a_number in a_list[:]:
            if a_number*b_number < max_score:
                a_list.remove(a_number)
                b_list.remove(b_number)
                answer_list.append([a_number,b_number])
                break

    print(answer_list)
    counter = len(answer_list)

    print(counter)
