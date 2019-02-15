def capitalize(s):
    pass
    res1 =''
    res2 = ''
    for i in range(1,len(s)+1):
        if(i%2==0):
            res1 += s[i-1].upper()
            res2 += s[i-1]
             
            #return res
        else:
            res1 += s[i-1] 
            res2 += s[i-1].upper() 
            
            #return s[i]
    return[res2,res1]

def capitalize2(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]
        
