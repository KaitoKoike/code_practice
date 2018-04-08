from decimal import *

deg , dis = map(int,input().split())
deg = deg / 10
dis = Decimal(dis) / Decimal(60)
dis = Decimal(dis).quantize(Decimal("0.1"),rounding=ROUND_HALF_UP)
dis = float(dis)
print(deg,dis)
if deg >= 168.75 and deg < 191.25:
    Dir="S"
elif deg >= 11.25 and deg < 33.75:
    Dir="NNE"
elif deg >= 191.25 and deg < 213.75:
    Dir="SSW"
elif deg >= 33.75 and deg < 56.25 :
    Dir="NE"
elif deg >= 213.75 and deg < 236.25:
    Dir="SW"
elif deg >= 56.25 and deg < 78.75 :
    Dir="ENE"
elif deg >= 236.25 and deg < 258.75 :
    Dir="WSW"
elif deg >= 78.75 and deg < 101.25 :
    Dir="E"
elif deg >= 258.75 and deg < 281.25 :
    Dir="W"
elif deg >= 101.25 and deg < 123.75 :
    Dir="ESE"
elif deg >= 281.25 and deg < 303.75 :
    Dir="WNW"
elif deg >= 123.75 and deg < 146.25 :
    Dir="SE"
elif deg >= 303.75 and deg < 326.25 :
    Dir="NW"
elif deg >= 146.25 and deg < 168.75 :
    Dir="SSE"
elif deg >= 326.25 and deg < 348.75 :
    Dir="NNW"
else:
    Dir = "N"

if 0.0 <= dis and dis <= 0.2 :
    w = 0
    Dir = "C"
elif 0.3 <= dis and dis <= 1.5:
    w = 1
elif 1.6 <= dis and dis <= 3.3:
    w = 2
elif 3.4 <= dis and dis <= 5.4:
    w = 3
elif 5.5 <= dis and dis <= 7.9:
    w = 4
elif 8.0 <= dis and dis <= 10.7:
    w = 5
elif 10.8 <= dis and dis <= 13.8:
    w = 6
elif 13.9 <= dis and dis <= 17.1:
    w = 7
elif 17.2 <= dis and dis <= 20.7:
    w = 8
elif 20.8 <= dis and dis <= 24.4:
    w = 9
elif 24.5 <= dis and dis <= 28.4:
    w = 10
elif 28.5 <= dis and dis <= 32.6:
    w = 11
elif 32.7 <= dis :
    w = 12

print(Dir,w)
