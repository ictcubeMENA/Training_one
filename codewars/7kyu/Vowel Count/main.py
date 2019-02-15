def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in ['a','e','u','i','o']:
            num_vowels += 1
        
    return num_vowels

def getCountB(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")