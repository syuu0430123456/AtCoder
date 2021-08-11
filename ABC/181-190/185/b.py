n,m,t = map(int,input().split())
rem = n
prev = 0 #直前のカフェ(orスタート地点を出た時間)

for _ in range(m):
    a, b = map(int,input().split())
    rem -= a - prev #直前のカフェ(orスタート)を出てからの残りバッテリー
    if rem <= 0:
        print("No")
        exit()
    rem += b-a
    rem = min(n, rem)
    prev = b

rem -= t - prev
if rem <= 0:
    print("No")
else:
    print("Yes")