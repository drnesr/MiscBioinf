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



#main
print NumberToPattern( 9904, 7 )
