def duplicate_count(text):
    # Your code goes here
    num_repeated_chars = 0
    for char in text.upper():
        count = text.upper().count(char)
        text = text.upper().replace(char,'')
        if count > 1 : 
            num_repeated_chars += 1
    return  num_repeated_chars

def duplicate_countB(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
