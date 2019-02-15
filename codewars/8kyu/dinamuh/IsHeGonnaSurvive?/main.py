def hero(bullets, dragons):
    mul = dragons * 2
    if bullets >= mul:
        return True
    else:
        return False


def hero2(bullets, dragons):
    return bullets >= dragons * 2
