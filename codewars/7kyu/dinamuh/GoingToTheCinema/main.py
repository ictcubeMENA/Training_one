import math
def movie(card, ticket, perc):
    i = 1
    total = 0
    while True :
        total+=ticket*math.pow(perc,i)
        if card+math.ceil(total)<i*ticket :
            break
        i+=1
    return i


def movie2(card, ticket, perc):
    num = 0
    priceA = 0
    priceB = card

    while math.ceil(priceB) >= priceA:
        num += 1
        priceA += ticket
        priceB += ticket * (perc ** num)

    return num