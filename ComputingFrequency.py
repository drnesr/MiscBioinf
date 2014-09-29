def LastSymbol( pattern ):

    return pattern[ -1: ]

   

def SymbolToNumber( symbol ):

    retVal = 10000

    if symbol == 'A':
        retVal = 0
        
    elif symbol == 'C':
        retVal = 1

    elif symbol == 'G':
        retVal = 2

    elif symbol == 'T':
        retVal = 3

    return retVal



def PatternToNumber( pattern ):

    #Important for exiting recursion.
    if pattern == "":
        return 0

    if len( pattern ) > 0:
        subStrEndIndex = len( pattern ) - 1
    else:
        subStrEndIndex = 0

    prunedPattern = pattern[ 0: subStrEndIndex ]

    lastSymbol = LastSymbol( pattern )

    return 4 * PatternToNumber( prunedPattern ) + SymbolToNumber( lastSymbol )



def ComputingFrequencies( text, k ):

    frequencyArray = []

    for itr in range( 0, 4 ** k ):
        frequencyArray.append( 0 )

    iterationSteps = len( text ) - k + 1

    for itr in range( 0, iterationSteps ):
        
        pattern = text[ itr: itr + k ]

        freqArrayIndex = PatternToNumber( pattern )

        frequencyArray[ freqArrayIndex ] = frequencyArray[ freqArrayIndex ] + 1


    return frequencyArray



#main
print ComputingFrequencies( "AAGCAAAGGTGGG", 2 )
