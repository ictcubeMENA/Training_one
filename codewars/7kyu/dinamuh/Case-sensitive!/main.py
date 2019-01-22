def case_sensitive(s):
    list=[]
    list2=[]
    for i in s:
        if i.isupper():
           list.append(i)
    if len(list)==0:
        list2.append(True)
        list2.append(list)
    else:
        list2.append(False)
        list2.append(list)
    return list2



def case_sensitive2(s):
    return [s.islower() or not s, [c for c in s if c.isupper()]]