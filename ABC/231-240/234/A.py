t = int(input())

def f(x):
    f = x*x + 2*x + 3
    return f
x = f(f(f(t)+t) + f(f(t)))
print(x)
