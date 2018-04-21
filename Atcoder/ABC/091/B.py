n = int(input())
word_list = {}

for i in range(n):
    s = input()
    if s not in word_list :
        word_list[s] = 1
    else:
        word_list[s] += 1

m = int(input())

for j in range(m):
    s = input()
    if s not in word_list:
        word_list[s] = -1
    else:
        word_list[s] -= 1
if max(word_list.values()) < 0:
    print(0)
else:
    print(max(word_list.values()))
