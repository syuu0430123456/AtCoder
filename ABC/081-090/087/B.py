a=int(input()) #500
b=int(input()) #100
c=int(input()) #50
x=int(input())

cnt = 0
for A in range(a+1):
    for B in range(b+1):
        for C in range(c+1):
            if 500*A + 100*B + 50*C == x:
                cnt +=1
print(cnt)