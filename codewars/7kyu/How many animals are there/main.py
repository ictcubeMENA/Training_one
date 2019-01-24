import re
def count_animals(sentence):
   return sum([int(n) for n in sentence.split() if n.isdigit()])

def count_animalsB(sentence):
    return sum(map(int, re.findall(r'\d+',sentence)))

#spent time for my solution: 0.03591169500000002
#spent time for the best practice : 0.06533677399999993