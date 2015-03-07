def myLogIter(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    power = 0
    log_b = 0
    
    while 1:
        log_b = b**power
        if log_b == x:
                break
        elif log_b > x:
            power -= 1
            break
        else:
            power += 1
    
    return power
  
