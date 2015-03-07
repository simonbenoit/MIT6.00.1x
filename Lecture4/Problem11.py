def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowel = ('a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U')
    
    if char in vowel:
        return True
    else:
        return False
