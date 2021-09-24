x = input()
n = int(input())
s = []
for _ in range(n):
    s.append(input())
print(s)
s.sort(key=x)
print(s)