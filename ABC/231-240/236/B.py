n = int(input())
a = list(map(int, input().split()))
a.sort()
a.append(0)

for i in range(n):
    if a[4*i+3] != i+1:
        print(i+1)
        exit()