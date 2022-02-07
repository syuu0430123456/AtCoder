A = list(map(int, input().split()))
A.sort()
cost = 0
for i in range(len(A)-1):
    cost += A[i+1] -A[i]
print(cost)