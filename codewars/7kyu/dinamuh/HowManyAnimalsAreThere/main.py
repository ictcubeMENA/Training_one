def count_animals(sentence):
  count=0
  for i in sentence.split():
      if i.isdigit():
          x=int(i)
          count+=x
  return count



import re

def CountAnimals(sentence):
    return sum(map(int, re.findall(r'\d+',sentence)))