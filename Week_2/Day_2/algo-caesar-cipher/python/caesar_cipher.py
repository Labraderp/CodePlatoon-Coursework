def upper_shift(ascii_code, shift):
    ceiling = 90

    new_ascii = ascii_code + shift
    if new_ascii > ceiling:
        new_ascii -= 26

    return chr(new_ascii)

def lower_shift(ascii_code, shift):
    ceiling = 122

    new_ascii = ascii_code + shift
    if new_ascii > ceiling:
        new_ascii -= 26

    return chr(new_ascii)


def caesar_cipher(string, shift_amount):
    #parse input into a usable format -- use ASCII characters
    #differentiate caps vs lower -- DONE, A = 65, Z = 90, a = 97, z = 122
    cipher_str = ''
    
    #shift lowercase and uppercase differently
    for char in string:
        cipher_char = ord(char)
        if cipher_char >= 65 and cipher_char <= 90:
            cipher_str += upper_shift(cipher_char, shift_amount)
        elif cipher_char >= 97 and cipher_char <= 122:
            cipher_str += lower_shift(cipher_char, shift_amount)
        else:
            cipher_str += char
       
    return cipher_str

print(caesar_cipher('What a string!', 5))