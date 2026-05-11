def isPalindrom(text):
    cleaned = "".join(filter(str.isalnum, text))
    return cleaned == stringReverse(cleaned)
    

def stringReverse(string_to_reverse):
    new_string=''
    index = len(string_to_reverse)
    list(string_to_reverse)
    while index:
        index -=1
        new_string += string_to_reverse[index]
    return new_string



print(isPalindrom("abc"))
print(isPalindrom("ab c"))
print(isPalindrom("abcba"))
print(isPalindrom("ab cba"))
