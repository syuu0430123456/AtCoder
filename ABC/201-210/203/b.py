n,k =map(int,input().split())
s = 0

for i in range(n):
    h = (i+1)*100
    for j in range(k):
        s += h + j +1
print(s)