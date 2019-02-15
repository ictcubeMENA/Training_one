def remove_every_other(my_list):
    # Your code here!
    i = 1
    x = len(my_list) / 2
    while i <= x:
        my_list.pop(i)
        i += 1

    return my_list


def remove_every_other2(my_list):
    return my_list[::2]
