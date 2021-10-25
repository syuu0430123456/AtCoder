h,w = map(int,input().split())
a = [list(map(int, input().split())) for i in range(h)]

ans = True
for i in range(h-1):
    for j in range(w-1):
        if not a[i][j] + a[i+1][j+1] <= a[i+1][j] + a[i][j+1]:
            ans = False
if ans:
    print("Yes")
else:
    print("No")