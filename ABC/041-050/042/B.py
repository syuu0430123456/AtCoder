n,l = map(int,input().split())
list = []
for _ in range(n):
    list.append(input())
list.sort()
print(''.join(list))