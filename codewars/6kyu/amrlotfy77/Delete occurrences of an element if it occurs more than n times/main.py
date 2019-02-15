def delete_nth(order,max_e):
    t = {}
    r = []
    for i in order:
      if i not in t :
        t[i] = 0
      else:
        t[i] += 1
      if t[i] <max_e:
        r.append(i)
    return r


def delete_nth1(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
