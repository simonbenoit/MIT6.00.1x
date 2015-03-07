def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i = 1
    gcd = 1
    
    while i <= min(a,b):
        if (a % i == 0) and (b % i == 0):
            gcd = i
        i += 1
    return gcd