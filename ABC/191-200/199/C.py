n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

amax = max(a)
bmin = min(b)

t = bmin - amax + 1
print(max(0,t))