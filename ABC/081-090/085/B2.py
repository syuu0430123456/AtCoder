n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))

d_set = set(d)
d = sorted(list(d_set))
print(len(d))