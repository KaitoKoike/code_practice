
phase = int(input())
loss_string = 0
correct_string = 0

for i in range(phase):
    x = input().split(" ")
    time = int(x[0])
    str_len = len(x[1])
    max_string = int(12*time/1000)
    if max_string < str_len:
        loss_string += str_len - max_string
        correct_string += max_string
    else:
        correct_string += str_len

print(correct_string,loss_string)
