def camel_case(string):
    
    
    string = str.title(string)
    re = string.replace(" ", "")
    return re

def camel_case1(string):
    return ''.join([i.capitalize() for i in string.split()])