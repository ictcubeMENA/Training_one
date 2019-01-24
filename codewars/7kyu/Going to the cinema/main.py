import math

def movie(card, ticket, perc):
    n = 1
    new_card =card + ticket * perc
    while math.ceil(new_card)  >= ticket * n:
        new_card = new_card + ticket * perc**(n+1)
        n += 1
        
    return n

def movieB(card, ticket, perc):
 num = 0
 priceA = 0
 priceB = card
 
 while math.ceil(priceB) >= priceA:
  num    += 1
  priceA += ticket
  priceB += ticket * (perc ** num)
  
 return num