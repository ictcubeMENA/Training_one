def compose(s1, s2):
    res =[]
    for c1,c2,i in zip(s1.split('\n'),s2.split('\n')[::-1],range(1,len(s1.split('\n'))+1)):
          res.append(c1[0:i] + c2[:len(s1.split('\n'))+1-i]) 
    return '\n'.join(res)   

def composeB(s1, s2):
    s1 = s1.split("\n")
    s2 = s2.split("\n")[::-1]
    
    n = len(s1)
    out = []
    
    for i in range(n):
        out.append(s1[i][:i+1] + s2[i][:(n-i)])
    
    return "\n".join(out) 