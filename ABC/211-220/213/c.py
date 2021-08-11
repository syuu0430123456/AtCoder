import numpy as np
h,w,n = map(int,input().split())
list = [0 for i in range(0,n)]

s = h*w
array_c=np.zeros(s).reshape(h,w)
for i in range(h):
    for j in range(w):
        array_c[i,j] = 5
print(array_c)
