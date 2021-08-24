a,b,w = map(int,input().split())

mi = -(-w*1000//b)
ma = w*1000//a
if mi >ma:
    print("UNSATISFIABLE")
else:
    print(mi,ma)