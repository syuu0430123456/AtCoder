n,d = map(int, input().split())
l = [list(map(int, input().split())) for l in range(n)]

cnt = 0
for i in range(n):
    xy = (l[i][0])**2 + (l[i][1])**2
    if xy <= d**2:
        cnt += 1
print(cnt)