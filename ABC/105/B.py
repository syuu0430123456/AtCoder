n=int(input())
cnt = 0
for i in range(100//4):
    for j in range(100//7):
        if 4*i+7*j==n:
            print("Yes")
            exit()
print("No")