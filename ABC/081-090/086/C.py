n = int(input())
t = [0]*n
x = [0]*n
y = [0]*n

for i in range(n):
    #上から順番に代入していく
    t[i], x[i], y[i] = map(int,input().split())

