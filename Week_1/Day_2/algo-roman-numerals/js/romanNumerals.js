exports.toRoman = function(num) {
        let numerals = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,
                        'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1};
        roman_str = '';
        for(val in numerals) {
          while(num >= numerals[val]) {
            roman_str += val;
            num -= numerals[val];
          }
        }
        return roman_str;
}