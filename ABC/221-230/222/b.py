n,p = map(int,input().split())
a = list(map(int,input().split()))

flag = 0
for i in range(n):
    if a[i] < p:
        flag += 1
print(flag)