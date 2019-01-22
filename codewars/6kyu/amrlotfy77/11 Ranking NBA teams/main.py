import re

def nba_cup(result_sheet, to_find):
    if to_find == '':
        return ''

    w = d = l = 0
    s = c = p = 0
    sp = result_sheet.split(',')
    print(sp)

    for g in sp:

        md = re.search('^(.*?) (\d+) (.*?) (\d+)$', g)

        if not md:
            return f'Error(float number):{g}'

        t1, s1, t2, s2 = md.groups()

        print(md.groups())

        score1 = int(s1)
        score2 = int(s2)
        if t1 == to_find:
            team, score, concede = t1, score1, score2
        elif t2 == to_find:
            team, score, concede = t2, score2, score1
        else:
            continue
        s += score
        c += concede
        if score > concede:
            w += 1
            p += 3
        elif score < concede:
            l += 1
            p += 0
        else:
            d += 1
            p += 1
    if w == d == l == 0:
        h = "{}:This team didn't play!".format(to_find)
        return h
    n= "{}:W={};D={};L={};Scored={};Conceded={};Points={}".format(to_find, w, d, l, s, c, p)
    return n


def nba_cup1(r, teamTarget):
    arr = r.split(',')
    checker = False
    result = ''
    arr1 = []

    if teamTarget == None: return []
    if teamTarget == '': return ''

    for a in arr:
        if '.' in a:
            checker = True
            result = "Error(float number):" + a
            return result

        "из строки выделить 2 команды и счет"

    def myFunc(stroka, teamTarget):
        score = [int(x) for x in stroka.split() if x.isdigit()]
        finder = stroka.index(str(score[0]))
        t0 = stroka[:finder - 1]  # название первой команды
        t1 = stroka[finder + len(str(score[0])) + 1: - len(str(score[1])) - 1]
        return ([t0, t1, score[0], score[1]])

    def counter(arr, teamtarget):
        W = D = L = Scored = Conc = Points = 0
        for x in arr:
            tarPos = x.index(teamTarget)
            print(x, tarPos)
            if tarPos == 0:
                if x[2] > x[3]:
                    W += 1
                    Points += 3
                if x[2] < x[3]:
                    L += 1
                if x[2] == x[3]:
                    D += 1
                    Points += 1
                Scored += x[2]
                Conc += x[3]
            if tarPos == 1:
                if x[3] > x[2]:
                    W += 1
                    Points += 3
                if x[3] < x[2]:
                    L += 1
                if x[3] == x[2]:
                    D += 1
                    Points += 1
                Scored += x[3]
                Conc += x[2]
        if teamTarget != '' and W == 0 and D == 0 and L == 0:
            return teamTarget + ":This team didn\'t play!"
        else:
            return teamTarget + ':W=' + str(W) + ';D=' + str(D) + ';L=' + str(L) + ';Scored=' + str(
                Scored) + ';Conceded=' + str(Conc) + ';Points=' + str(Points)

    if not checker:
        for x in arr:
            arr1.append(myFunc(x, teamTarget))
        arr = []
        for x in arr1:
            if teamTarget in x:
                arr.append(x)

    return (counter(arr, teamTarget))