n = int(input())
a = list(map(int,input().split()))
x = int(input())

cnt = 0
s = sum(a)
y = x//s
ans = s*y
cnt += y*n
for i in range(n):
    ans += a[i]
    if ans > x:
        print(cnt+1+i)
        exit()
