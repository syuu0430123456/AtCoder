a,b,c,d = map(int,input().split())
cc = 0 #No
ans = 0
for i in range(100000):
    a += b
    cc += c
    if a > cc*d:
        ans += 1
        if ans > 99999:
            print(-1)
    else:
        ans += 1
        print(ans)
        break

