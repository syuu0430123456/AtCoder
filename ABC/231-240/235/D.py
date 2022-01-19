n,q = map(int, input().split())
a = list(map(int, input().split()))

cnt_p = 0
for i in range(q):
    x,k = map(int,input().split())
    cnt = a.count(x)
    cnt += cnt_p
    for j in range(n):
        if cnt >= k:
            if a[j] == x:
                print(j+1)
                a[j] = -1
                cnt_p += 1
                break
        
        print(-1)
        break
           
print(a)
