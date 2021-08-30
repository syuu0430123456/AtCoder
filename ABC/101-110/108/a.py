s,p = map(int,input().split())

#n + m = s
#n * m = p
div = []
for i in range(1,int(p**0.5+1)):
    if p%i==0:
        div.append(i)
        if i != p//i:
            div.append(p//i)
            if div[0]+div[1]==s:
                print("Yes")
                exit()
print("No")