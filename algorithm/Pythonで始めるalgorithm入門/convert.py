n = 18

def conver(n,base):
    result = ''

    while n > 0:
        result = str(n % base) + result
        n //= base

    return result

print(conver(n, 2))
print(conver(n, 3))
print(conver(n, 8))