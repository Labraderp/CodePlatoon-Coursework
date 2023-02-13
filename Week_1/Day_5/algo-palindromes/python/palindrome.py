def palindrome(word):
    word = str(word).lower()    #cast input to string and make lowercase
    lst = []        
    
    for letter in word:         #for each char in the input string...
        if letter.isalnum():    #... if the char is a-z0-9...
            lst.append(letter)  #add to array!
    
    return lst == lst[::-1]     #compare the list frontwards and backwards :D

palindrome("race!@#!$car")