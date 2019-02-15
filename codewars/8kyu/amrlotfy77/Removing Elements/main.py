def remove_every_other(my_list):
    del my_list[1::2]
    return my_list


def remove_every_other1(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]