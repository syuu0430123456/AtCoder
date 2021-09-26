a,b,c = map(int,input().split())

d = 1000//c + 1

for i in range(d):
    if a <= c*i <= b:
        print(c*i)
        exit()
print(-1)