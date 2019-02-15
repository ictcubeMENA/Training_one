def generateShape(int):
    space = ''
    shape = '+'
    st= ''
    for i in range (0,int):
        space += (shape*int) + '\n' 
    for i in range (0,int):
        st += (shape *int) + '\n'
        
    return st[0:-1]
     
        
def generateShape2(n):
    return '\n'.join('+'*n for i in range(n))