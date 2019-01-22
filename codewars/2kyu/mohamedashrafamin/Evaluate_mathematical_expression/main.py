def calc(expression):
    if expression == 'eval':
        return []
    return eval(expression)





print(calc("-7 * -(6 / 3)"))