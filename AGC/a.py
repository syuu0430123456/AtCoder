n , x = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
cnt = 0

for i in a:
    x -= i
    if x >= 0:
        cnt += 1
    else:
        break
if x > 0:
    cnt -= 1
print(cnt)