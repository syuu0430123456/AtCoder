x1,y1,x2,y2 = map(int,input().split())

#点Pを(x,y)とする。A(x1,y1), B(x2,y2)
#AP^2 = (x-x1)^2+(y-y1)^2 = 5
#BP^2 = (x-x2)^2+(y-y2)^2 = 5

#AP^2=BP^2
#-2xx1+x1^2 + -2yy1 +y1^2 = -2xx2 +x2^2 + -2yy2 +y1^2
# 2x(x2-x1)+2y(y2-y1)+x1^2+x2^2-x2^2^y2^2 = 0
for x in range(x1-3,x1+3):
    print(x)
    for y in range(y1-3,y1+3):
        if (x-x1)**2+(y-y1)**2 == (x-x2)**2+(y-y2)**2 == 5:
            print("Yes")
            exit()
print("No")                