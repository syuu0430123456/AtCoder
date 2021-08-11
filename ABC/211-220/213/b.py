n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
#print(a)
#print(b)
for i in range(n):
    if a[i]==b[-2]:
        print(i+1)

