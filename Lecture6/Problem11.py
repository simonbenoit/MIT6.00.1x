def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for k in aDict.keys():
        if len(aDict[k]) >= biggestValue:
            result = k
            biggestValue = len(aDict[k])
    return result
