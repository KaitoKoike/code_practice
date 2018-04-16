s = list(input())
score = 0

for hit in s:
    if hit == "0":
        score += 10
    else:
        score += int(hit)
print(score)
