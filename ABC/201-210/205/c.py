a,b,c = map(int,input().split())
if abs(a) == abs(b):
    print("=")
    exit()
if c%2==0:
    if abs(a)>abs(b):
        print('>')
    else:
        print('<')
else:
    if a>b:
        print('>')
    else:
        print('<')