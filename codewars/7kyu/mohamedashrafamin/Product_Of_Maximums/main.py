def max_product(lst, n_largest_elements):
    lst = sorted(lst,reverse= True)
    res= 0
    for i in range(n_largest_elements):
        res *= lst[i]
    return res