n = int(input())
s_n = str(n)
ans = 0

for i in range(1,n+1):
    if len(s_n) == 1 or len(s_n)==3 or len(s_n)==5:
       ans += 1
print(ans)