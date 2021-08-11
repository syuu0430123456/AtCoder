n = int(input())
t = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    p = t[i][-1] - t[i][0] +1
    ans += p*(t[i][0]+t[i][-1])/2

print(int(ans))