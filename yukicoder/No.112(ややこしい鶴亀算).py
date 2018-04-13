N = int(input())

foot_list = list(map(int,input().split()))
sum_number_foot = int(sum(foot_list)/ (N-1))
#print(sum_number_foot)

for i,count_foot in enumerate(foot_list):
    foot_list[i] = sum_number_foot - count_foot

#print(foot_list)
turtol = foot_list.count(4)
vine = foot_list.count(2)

print(vine,turtol)
