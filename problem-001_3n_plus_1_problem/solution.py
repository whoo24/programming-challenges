def is_odd(n):
    if (n % 2) == 0:
        return False
    return True

def func(n, length):
    
    if n == 1:
        return length
    
    if is_odd(n):
        n = n * 3 + 1
    else:
        n = n / 2
    
    return func(n, length+1)

def solve(i, j):
    length = 0
    for k in range(i, j):
        length = max( length, func(k, 1) )
    return length

# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
i = 100
j = 200
print '%d %d %d' % (i, j, solve(i, j) )

