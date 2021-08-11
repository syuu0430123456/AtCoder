n,y = map(int,input().split())

for a in range(n+1):
    for b in range(n-a+1):
        if y == 1000*a + 5000*b + (n-a-b)*10000:
            print(n-a-b, b, a)
            exit()
print(-1,-1,-1)