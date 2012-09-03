from sys import stdin, stdout

def is_odd(n):
    if (n % 2) == 0:
        return False
    return True

def func(n, length):
    
    if n == 1:
        return length
    
    #if is_odd(n):
    #    n = n * 3 + 1
    #else:
    #    n = n >> 1

    if is_odd(n):
        n = n * 3 + 1
        length += 1
        
    n = n >> 1
    
    return func(n, length+1)

def solve(i, j):

    length = 0
    for k in range(i, j):
        length = max( length, func(k, 1) )
    return length

# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
inputs = []
while(True):
    try:
        line = raw_input()
        
        a, b = line.split()
        inputs.append( [int(a), int(b)] )

    except Exception, e:
        break;

for input_pair in inputs:
    i, j = min( input_pair[0], input_pair[1] ), max( input_pair[0], input_pair[1] )

    print( '%d %d %d' % ( input_pair[0], input_pair[1], solve(i, j) ) )
