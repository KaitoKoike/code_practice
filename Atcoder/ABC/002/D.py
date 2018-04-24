n, m = map(int,input().split())
relation_list = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    relation_list[a-1][b-1]=relation_list[b-1][a-1]= 1
    relation_list[a-1][a-1]= relation_list[b-1][b-1] = 1
#print(relation_list)
ans = 1

for i in range(1<<n):
    person_list = list()
    for j in reversed(range(1,n+1)):
        if i&(1<<j-1):
            person_list.append(j)
    #print(person_list)
    flag = 0
    for person_a in person_list:
        for person_b in person_list:
            if relation_list[person_a-1][person_b-1] != 1 :
                flag = -1
    if flag == 0:
        ans = max(ans,len(person_list))
print(ans)
