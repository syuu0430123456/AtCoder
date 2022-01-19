n,y = map(int,input().split())

for a in range(n+1):
    for b in range(n+1-a):
        if y == 10000*a + 5000*b + 1000*(n+1-a-b):
            print(a,b,n+1-a-b)
            exit()
print(-1,-1,-1)