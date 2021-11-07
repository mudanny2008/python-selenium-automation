#Split in Half
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


string = 'bbbbbcaaaaa'
Result = 'aaaaabbbbbc'

def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
        add = 1

    left = s[:half + add]
    right = s[half + add:]


    return right + left

print(split_in_half(string))


#Unique Characters in String
#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

def uni_char(s):
    return len(set(s)) == len(s)


posit_string = 'abcde'
negat_string = 'aabcde'

print(uni_char(posit_string))
print(uni_char(negat_string))



