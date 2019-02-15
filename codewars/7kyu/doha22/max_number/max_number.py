def max_number(n):
    sorting ="".join(sorted(str(n), reverse = True)) 
    s =int(sorting)
    return s

def max_number2(n):
    return int(''.join(sorted(str(n), reverse=True)))
    
