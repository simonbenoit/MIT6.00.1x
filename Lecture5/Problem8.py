def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    def middle(aStr):
        '''
        aStr: a string
        
        returns: the middle character of the string
        '''
        return aStr[len(aStr)//2]
    
    if aStr == '':
        return False
    elif char == aStr:
        return True
    elif middle(aStr) == char:
        return True
    elif char > middle(aStr):
        return isIn(char, aStr[(len(aStr)/2)+1:])
    elif char < middle(aStr):
        return isIn(char, aStr[:(len(aStr)/2)]) 
    else:
        return False  