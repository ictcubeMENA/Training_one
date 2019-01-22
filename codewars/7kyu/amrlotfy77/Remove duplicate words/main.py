def unique(integers):
    final_list = []
    for num in integers:
        if num not in final_list:
            final_list.append(num)
    return final_list


def unique1(integers):
    ans = []
    for x in integers:
        if x not in ans:
            ans.append(x)
    return ans
