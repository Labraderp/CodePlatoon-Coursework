def char_count(string):
  #Dictionary for input
  char_dict = {}
  for letter in string:
    if letter.isalpha():
      if letter not in char_dict:
        char_dict.update({letter: 1})
      else:
        char_dict[letter] += 1

    sorted_dict = sorted(char_dict.items(), key = lambda kv: kv[1], reverse=True)
  
  ret_arr = []
  for keys in sorted_dict:
    ret_arr.append([keys[0], keys[1]])

  print(ret_arr)
  return(ret_arr)