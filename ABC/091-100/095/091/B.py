n = int(input())
red = [input() for _ in range(n)]
m = int(input())
blue = [input() for _ in range(m)]

ans = 0
for i in red:
    x = red.count(i)
    y = blue.count(i)
    ans = max(ans,x-y)
print(ans)