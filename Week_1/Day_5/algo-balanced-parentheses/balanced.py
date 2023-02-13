def balanced(some_str):
    #Some way to parse the input - DONE
    #Track open/closed paren
    #Compare open vs closed (in line?)
    #Statements: When to fail, notably
    if not len(some_str) % 2 == 0:
        return False
    
    braces = {'(' : 0, '[' : 0, '{' : 0}
    last_brace = ''
    for char in some_str:
        match char:
            case '(':
                last_brace += '('
                braces[char] += 1
            case '[':
                last_brace += '['
                braces[char] += 1
            case '{':
                last_brace += '{'
                braces[char] += 1
            case ')':
                if not last_brace == '(':
                    return False
                last_brace = last_brace[0:len(last_brace)-1]
                braces['('] -= 1
                if braces['('] < 0:
                    return False
            case ']':
                if not last_brace == '[':
                    return False
                last_brace = last_brace[0:len(last_brace)-1]
                braces['['] -= 1
                if braces['['] < 0:
                    return False
            case '}':
                if not last_brace == '{':
                    return False
                last_brace = last_brace[0:len(last_brace)-1]
                braces['{'] -= 1
                if braces ['['] < 0:
                    return False
    return True

print(balanced('{[]}'))