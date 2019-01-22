def my_parse_int(string):
    if string.strip().isdigit():
        return int(string)

    return "NaN"


def my_parse_int1(s):
    try:
        return int(s)
    except ValueError:
        return 'NaN'
