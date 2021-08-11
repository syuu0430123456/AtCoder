import math
p = int(input())
cnt = 0
m=0
for i in reversed(range(1,11)):
    m = math.factorial(i)
    if p//m != 0:
        cnt += p//m
        p = p-p//m * m
print(cnt)