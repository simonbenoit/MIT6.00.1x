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

