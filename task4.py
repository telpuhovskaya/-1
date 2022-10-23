def squareRoot(x):
    def squareRootIteration(guessNumber):
        if isGoodEnough(guessNumber):
            return guessNumber
        else:
            return squareRootIteration(improveNumber(guessNumber))
        
    def improveNumber(guessNumber):
        return average(guessNumber, x/guessNumber)
    
    def average(x, y):
        return (x+y)/2
    
    def isGoodEnough(guessNumber):
        if(abs(guessNumber**2-x)<0.001):
            return 1
        else:
            return 0
        
    return squareRootIteration(1.0)
