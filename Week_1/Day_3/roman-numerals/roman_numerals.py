def to_roman(num):
    output = ''

    numerals = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,
                'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
    
    for key in numerals:
        arabic_numeral = numerals[key]

        while num >= arabic_numeral:
            output += key
            num -= arabic_numeral

    return output

print(to_roman(2746))