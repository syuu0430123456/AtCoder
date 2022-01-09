N = int(input())
z = [list(map(int, input().split())) for z in range(N)]

import math

def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    return d
x = 0
for i in range(N-1):
    for j in range(i+1, N):
        d = get_distance(z[i][0], z[i][1], z[j][0], z[j][1])
        x = (max(x,d))
print(x)