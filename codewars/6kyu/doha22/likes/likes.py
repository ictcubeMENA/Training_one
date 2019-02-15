def likes(names):
    text =""
    if len(names)==0 :
        #return []
        return text + "no one likes this"     
    elif len(names) == 1:
        return str(names[0]) + " likes this"
    elif len(names) > 1 and  len(names) < 4 :
        for i in range(0 , len(names)-1 ):
             text = text + names[i] + ", "
        text = text[:-2]
        return text + " and " + str(names[len(names) - 1]) + " like this"
    else :
        for i in range(0, 2):
            text = text + names[i] + ", "
        text = text[:-2]
        return text + " and " + str(len(names)-2) + " others like this"

def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)