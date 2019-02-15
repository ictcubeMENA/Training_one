def play_pass(s, n):
    lst = []
    for c in s:
        if c.isalpha(): 
            ord_char= ord(c)+n
            if ord_char > 90:
                ord_char = ord_char-90+64
            lst.append(chr(ord_char))
        elif c.isdigit():
            lst.append(str(9-int(c)))
        else:
            lst.append(c)
    s = ''.join(lst)
    r = ['']*len(s)
    r[::2] = s[::2].upper()
    r[1::2] = s[1::2].lower()
    return ''.join(r)[::-1]


def play_passB(s, n):

    # Step 1, 2, 3
    shiftText = ""
    for char in s:
        if char.isdigit():
            shiftText += str(9 - int(char))
        elif char.isalpha():
            shifted = ord(char.lower()) + n
            shiftText += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
        else:
            shiftText += char

    # Step 4
    caseText = ""
    for i in range(len(shiftText)):
        caseText += shiftText[i].upper() if i % 2 == 0 else shiftText[i].lower()

    # Step 5
    return caseText[::-1]
