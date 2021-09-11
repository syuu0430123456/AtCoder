n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]


for p in [x[::-1] for x in list(zip(*s))]:
    print("".join(p))

