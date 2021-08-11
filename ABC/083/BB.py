n,a,b = map(int,input().split())
cnt = 0
tot=0
for i in range(0, n):
    t=str[i]
    for j in range(len(t)):
        tot += t[j]
    if a<= tot <=b:
        cnt+=1
print(cnt)
