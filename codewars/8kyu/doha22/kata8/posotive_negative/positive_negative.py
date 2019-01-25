def count_positives_sum_negatives(arr):
    res_num = [0,0]
    if (arr == [] ):
        return []  
    for n in arr:
        if(n> 0 ):
            res_num[0] += 1
        elif(n < 0):
          
            res_num[1] += n
    return res_num
    
def count_positives_sum_negatives2(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []