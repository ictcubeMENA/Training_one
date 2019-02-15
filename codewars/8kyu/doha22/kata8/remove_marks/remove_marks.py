def remove_exclamation_marks(s):
    #your code here
    return s.replace('!','')
        

    

def remove_exclamation_marks2(s):
    return ''.join([x for x in s if x != '!'])