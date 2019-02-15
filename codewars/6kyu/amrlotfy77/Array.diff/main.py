def array_diff(a, b):
    for i in b:
      if i in a:
        for j in range(a.count(i)):
          a.remove(i)
    return a


def delete_nth1(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
