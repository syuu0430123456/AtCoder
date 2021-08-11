#h,wを入力
h,w = map(int,input().split())
#リスト内包表記
#上から順にlistを読み込んでlistに格納
a = [list(map(int,input().split())) for i in range(h)]
#aの各リストの最小値を格納するmin_listを作成
#min_listの中の最小をminに代入
min_list = []
ans = 0
for i in range(h):
    a[i].sort()
    min_list.append(a[i][0])
min = min(min_list)
#全てのa[i][j]に対してminとの差を計算しansに代入
for x in range(h):
    for y in range(w):
        ans += a[x][y] - min
print(ans)