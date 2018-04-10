

taro_suggest_list = []
all_turn = int(input())


for turn in range(all_turn):
    number_list = [ i for i in range(10) ]
    taro_suggest_and_answer = input().split(" ")

    taro_suggest = list(map(int,taro_suggest_and_answer[:4]))

    answer = taro_suggest_and_answer[4]

    if answer =="YES":
        taro_suggest_list.append(taro_suggest)
    else:
        for number in taro_suggest:
            number_list.remove(int(number))
        taro_suggest_list.append(number_list)

answer_list = [t for t in taro_suggest_list[0]]

for n in taro_suggest_list[0]:
    for i in range(all_turn):
        if n not in taro_suggest_list[i]:
            if n in answer_list:
                answer_list.remove(n)

print(answer_list[0])
