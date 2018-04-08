def d_precipitation(N,TIME):
    time = []
    for rain in TIME:
        #開始時間と終了時間を00:00を始点として計算し、単位を分として１次元に落とす
        start = int(rain[0:2]) * 60 + int(rain[2:4])
        end = int(rain[5:7]) * 60 + int(rain[7:9])
        start -= start%5 #５で割ったあまりを引いて5分単位に丸める
        end += (5 - (end % 5)) % 5 #直後の5分単位に丸める
        time.append((start,end))
    time.sort()

    #累積和を求める
    time_part = [0 for i in range(1442)]
    for start , end in time:
        time_part[start] += 1
        time_part[end+1] -= 1
    for i in range(len(time_part) - 1):
        time_part[i + 1] += time_part[i]

    #1以上の要素が出てきた区間をs,eに詰める(s[i],e[i]が開始ー終了時刻の組み)
    s,e = [],[]
    is_zero = True
    for i ,t in enumerate(time_part):
        if t > 0 and is_zero:
            s.append(i)
            is_zero = False
        if t == 0 and not is_zero:
            e.append(i-1)
            is_zero=True
    ans = ""
    for start,end in zip(s,e):
        ans += "{0:02d}{1:02d}-{2:02d}{3:02d}\n".format(start // 60 ,start%60,end//60,end%60)
    return ans[:-1]

N = int(input())
TIME = [input() for i in range(N)]
print(d_precipitation(N,TIME))
