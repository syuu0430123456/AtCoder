n = int(input())
l = [list(map(str,input().split())) for l in range(n)]

for i in range(n-1):
    for j in range(i+1,n):
        if l[i][0]==l[j][0]:
            if l[i][1]==l[j][1]:
                print("Yes")
                exit()
print("No")