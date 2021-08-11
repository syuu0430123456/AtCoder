n,k = map(int,input().split())
cnt = 0
for i in range(35):
    if n//k >= 0:
        n = n//k
        if n == 0:
            print(i+1)
            exit()
