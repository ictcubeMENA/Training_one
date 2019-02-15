def decodeMorse(morseCode):
    results = []
    for item in morseCode.split(' '):
        results.append(MORSE_CODE.get(item))
        s = ""
        t = 0
        print(results)
        for i in range(len(results)):
            if results[i] is None:
                t += 1
            else:
                if t == 2:
                    s += " "
                    t = 0
                    continue
                elif t == 3:
                    t = 0
                    s += results[i]
                    continue
                s += results[i]
    return s
