import math
n = int(input())
x = list(map(int, abs(input().split())))
ans1 = 0
ans2 = 0
for i in range(n):
    ans1 += x[i]
    ans2 += abs(x[i])**2
    ans3 = max(abs(x[i],0)

print(ans1) #マンハッタン距離
print(math.sqrt(ans2)) #ユークリッド距離
print(ans4)
