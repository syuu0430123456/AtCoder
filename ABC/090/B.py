a,b = map(int,input().split())
ans = 0
for i in range(a,b+1):
    tmp = i
    s = str(i)
    s_rev = ''.join(list(reversed(s)))
    if s == s_rev:
        ans += 1
print(ans)