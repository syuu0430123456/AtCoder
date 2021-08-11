a,b,c=map(int,input().split())
if c==0 and a>b:
    print("Takahashi")
elif c==0 and a<=b:
    print("Aoki")
else:
    if a>=b:
        print("Takahashi")
    else:
        print("Aoki")