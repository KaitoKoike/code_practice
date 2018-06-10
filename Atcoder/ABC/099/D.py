import itertools

N,C = map(int,input().split())
C_list = [i for i in range(C)]
D = []
for i in range(C):
    D_item = list(map(int,input().split()))
    D.append(D_item)
c = [[]for i in range(3)]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        c[(i+j+2)%3].append(tmp[j])

#3色選ぶ
choose_C_list = list(itertools.permutations(C_list,3))
Iwakan = 1e+10
for choose_C in choose_C_list:
    tmp_Iwakan = 0
    for i in range(3):
        for cell in c[i]:
            tmp_Iwakan += D[cell-1][choose_C[i]-1]
    Iwakan = min(Iwakan,tmp_Iwakan)

print(Iwakan)
