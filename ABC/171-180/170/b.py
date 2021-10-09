x,y = map(int,input().split())

min = 2*x
max = 4*x
ans = "No"
if y %2 == 0:
    if min <= y <= max:
        ans = "Yes"
print(ans)