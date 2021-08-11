sx, sy, gx, gy = map(int,input().split())
sy = - sy
# a:傾き b:切片
a = (gy-sy)/(gx-sx)
b = gy - a*gx
x = -b/a
print(x)