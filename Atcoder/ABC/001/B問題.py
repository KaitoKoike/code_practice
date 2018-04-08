#kmに変換
m = int(input())/1000

if m < 0.1:
    vv = 0
elif 0.1 <= m and m <= 5 :
    vv = m * 10
elif 6 <= m and m <= 30:
    vv = m + 50
elif 35 <= m and m <= 70:
    vv = ((m - 30) / 5 ) + 80
elif 70 < m :
    vv = 89

vv_padded = '%02d'%vv
print(vv_padded)
