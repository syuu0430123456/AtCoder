n = int(input())
a = list(map(int,input().split()))
l = []
for i in range(n):
    l.append(i+1)
a.sort()
if a == l:
    print("Yes")
else:
    print("No")