k = int(input())
a,b = map(int,input().split())

if a%k==0:
    print("OK")
else:
    if ((a//k)+1)*k <=b:
        print("Ok")
    else:print("NG")
