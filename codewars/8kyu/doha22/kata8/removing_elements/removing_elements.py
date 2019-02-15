def remove_every_other(my_list):
    # Your code here!
    a = my_list[::2]
    return a

def remove_every_other2(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]