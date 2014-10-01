CONST_NUCLEOTIDE_MULTIPLE = 4



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

    for itr in range( 0, CONST_NUCLEOTIDE_MULTIPLE ** k ):
        frequencyArray.append( 0 )

    iterationSteps = len( text ) - k + 1

    for itr in range( 0, iterationSteps ):
        
        pattern = text[ itr: itr + k ]

        freqArrayIndex = PatternToNumber( pattern )

        frequencyArray[ freqArrayIndex ] = frequencyArray[ freqArrayIndex ] + 1


    return frequencyArray



def NumberToSymbol( index ):

    symbol = 'Z'

    if index == 0:
        symbol = 'A'

    elif index == 1:
        symbol = 'C'

    elif index == 2:
        symbol = 'G'

    elif index == 3:
        symbol = 'T'

    return symbol



def NumberToPattern( index, k ):

    if k == 1:
        return NumberToSymbol( index )

    prefixIndex = index // 4

    remainder = index % 4

    prefixPattern = NumberToPattern( prefixIndex, k - 1 )

    symbol = NumberToSymbol( remainder )

    return prefixPattern + symbol



def FasterFrequentWords( text, k ):
    
    frequentPatterns = []

    frequencyArray = ComputingFrequencies( text, k )

    maxCount = 0

    for itr in range( 0, len( frequencyArray ) ):

        if frequencyArray[ itr ] > maxCount:
            maxCount = frequencyArray[ itr ]
    

    for itr in range( 0, CONST_NUCLEOTIDE_MULTIPLE ** k ):
        
        if frequencyArray[ itr ] == maxCount:

            pattern = NumberToPattern( itr, k )

            frequentPatterns.append( pattern )


    return frequentPatterns



#main
print FasterFrequentWords( "AAGCAAAGGTGGG", 2 )
