def comb(fruits):
    if len(fruits) == 0 or len(fruits) == 1:
        return 0
    a = []
    cnt = 0
    t = sum(fruits)
    while len(fruits) > 1:
        fruits.sort() 
        fruits[0] = fruits[0] + fruits[1]  
        fruits.pop(1) 
        a.insert(cnt, fruits[0])  
        cnt += 1
    return sum(a)

def comb1(fruits):
    energy = 0
    if len(fruits) == 1:
        return 0
    while len(fruits) != 1:
        fruits.sort()
        delta = sum(fruits[:2])
        energy += delta
        fruits = [delta] + fruits[2:]
    return energy