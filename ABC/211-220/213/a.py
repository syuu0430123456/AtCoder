a,b = map(int,input().split())
for i in range(1000):
    if a^i==b:
        print(i)
