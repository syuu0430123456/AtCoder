n,d = map(int,input().split())
a = [list(map(int, input().split())) for l in range(n)]
cnt = 0
for i in range(n-1):
    for j in range(i+1,n):
        total = 0
        for k in range(d):
            total += abs(a[i][k]-a[j][k])**2

        for l in range(1,int(total**(1/2)+1)):
            if l **2 == total:
                cnt +=1
print(cnt)
