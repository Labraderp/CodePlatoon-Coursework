def credit_check(string):
    num_str = []
    
    # DONE - way to process array, right to left
    # double every other index
    # collapse double-digits into single digit (n-9)
    
    for i in string:
        num_str.append(int(i))
    chk_digit = num_str[-1]

    for i in range(len(num_str)-2, -1, -2):
        hold = num_str[i] * 2
        if hold > 9:
            hold -= 9
        num_str[i] = hold

    # sum all digits
    total = sum(num_str) - chk_digit
    # modulo 10, return strings!

    dig_check = (10 - (total % 10)) % 10
    print(dig_check)
    if dig_check == chk_digit:
        #print(mod_chk)
        return "The number is valid!"
    else:
        #print(mod_chk)
        return "The number is invalid!"
    
#print(credit_check("6011797668867828"))