def PatternCount( text, pattern ):
    count = 0
    textParseSize = len( text ) - len( pattern ) + 1
            
    for itr in range( 0, textParseSize ):
   
        if( text[ itr : itr + len( pattern ) ] == pattern ):
            count = count + 1
    
    
    return count



text1 = "ACAACTATGCATACTATCGGGAACTATCCT"
pattern1 = "ACTAT"

print PatternCount( text1, pattern1 )

text2 = "CGATATATCCATAG"
pattern2 = "ATA"

print PatternCount( text2, pattern2 )
