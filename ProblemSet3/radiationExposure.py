def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    
    def f(x):
        import math
        #return 10*math.e**(math.log(0.5)/5.27 * x)
        return 60*math.e**(math.log(0.5)/55.6 * x)
        #return 150*math.e**(math.log(0.5)/32.2 * x)
        #return 200*math.e**(math.log(0.5)/14.1 * x)
        #return 400*math.e**(math.log(0.5)/3.66 * x)

    result= 0
    i = start
    
    while i < stop:
        result += f(i)*step
        i += step
    return result