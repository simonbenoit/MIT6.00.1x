#problem 4
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
  
#problem 5                            
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    s3 = ''
    i = 0
    
    while i < min(len(s1), len(s2)):
        s3 += s1[i]+s2[i]
        i += 1
    if i == len(s1):
        s3 += s2[i:]
    elif i == len(s2):
        s3 += s1[i:]            
    return s3 

#problem 6
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0]+ s2[0])
    return helpLaceStrings(s1, s2, '')

#problem 7     
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n == 0:
        return True
    if n < 0:
        return False
    elif McNuggets(n-6) or McNuggets(n-9) or McNuggets(n-20):
        return True
    return False

#problem 8.1
def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess
    
#def sqrt(a):
#    def tryit(x):
#        return 0.5 * (a/x + x)
#    return fixedPoint(tryit, 0.0001)
    
def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)