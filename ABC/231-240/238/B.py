N = int(input())
A = list(map(int, input().split()))

angle = 0
B = [0]
for a in A:
    angle += a
    B.append(angle%360)
B.sort()
B.append(360)
m = 0
for i in range(len(B)-1):
    m = max(B[i+1]-B[i], m)
print(m)