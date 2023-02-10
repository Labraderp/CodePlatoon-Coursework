# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
    string1 = string1.lower().replace(' ', '')
    string2 = string2.lower().replace(' ', '')
    letter_dict1 = {}
    letter_dict2 = {}
    
    for letter in string1:
        # print(letter)
        if letter in letter_dict1:
            letter_dict1[letter] += 1
        else:
            letter_dict1.update({letter:1})
   
    for letter in string2:
        # print(letter)
        if letter in letter_dict2:
            letter_dict2[letter] += 1
        else:
            letter_dict2.update({letter:1})
        
    # for key in letter_dict1:
    #     if key in letter_dict2:
    #         if letter_dict1[key] == letter_dict2[key]:
    #             continue
    #         else:
    #             return False
    #     else:
    #         return False
    # return True
    print(letter_dict1)
    print(letter_dict2)
    if letter_dict1 == letter_dict2:
        return True
    return False
    

# Part 2
def anagrams_for(word, list_of_words):
    string1 = word.lower()
    letter_dict1 = {}
    answer = []
    for letter in string1:
        # print(letter)
        if letter in letter_dict1:
            letter_dict1[letter] += 1
        else:
            letter_dict1.update({letter:1}) 
 
    for string2 in list_of_words:
        string2 = string2.lower()
        letter_dict2 = {}
        flag = True
        for letter in string2:
        # print(letter)
            if letter in letter_dict2:
                letter_dict2[letter] += 1
            else:
                letter_dict2.update({letter:1})

        for key in letter_dict1:
            if key in letter_dict2:
                if letter_dict1[key] == letter_dict2[key]:
                    continue
                else:
                    flag = False
            else:
                flag = False
    
        if flag == True:
            answer.append(string2)
    
    return answer
    


list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds", "pplea"]

#print(anagrams_for("threads", list_of_words)) #== ["threads", "trashed", "hardest", "hatreds"])
#print(anagrams_for("apple", list_of_words)) #== [])


print(is_character_match('Anna Madrigal', 'A man and a girl')) 
print(is_character_match('charm', 'march'))                     
print(is_character_match('zach', 'attack'))                     
print(is_character_match('CharM', 'mARcH'))
print(is_character_match('abcde2', 'c2abed'))