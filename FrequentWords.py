def PatternCount( text, pattern ):

    count = 0
    textParseSize = len( text ) - len( pattern ) + 1
            
    for itr in range( 0, textParseSize ):
   
        if( text[ itr : itr + len( pattern ) ] == pattern ):
            count = count + 1
    
    
    return count






def FrequentWords( text, patternSize ):

    frequentPatterns = []
    textParseSize = len( text ) - patternSize + 1
    
    #Initializing patternCount to 0
    patternCount = []
    for itr in range( 0, textParseSize ):
        
        patternCount.append( 0 )

        
    #Populating patternCount
    for itr in range( 0, textParseSize ):

        pattern = text[ itr : itr + patternSize ]

        patternCount[ itr ] = PatternCount( text, pattern )


    #Finding the maxium value(count) within patternCount.
    maxCount = 0
    for itr in range( 0, len( patternCount ) ):

        if( patternCount[ itr ] > maxCount ):
            maxCount = patternCount[ itr ]


    #Populating frequentPatterns
    for itr in range( 0, len( patternCount ) ):

        if( patternCount[ itr ] == maxCount ):
            frequentPatterns.append( text[ itr : itr + patternSize ] )

    return frequentPatterns



    

#Main
text1 = "ACTGACTCCCACCCC"

frequentWords = FrequentWords( text1, 3 )

print frequentWords
