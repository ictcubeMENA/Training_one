def set_alarm(employed, vacation):
    # Your code here
  if(employed == True and vacation == False):
      return True 
  else:
      return False

def set_alarm2(employed, vacation):
    return employed and not vacation