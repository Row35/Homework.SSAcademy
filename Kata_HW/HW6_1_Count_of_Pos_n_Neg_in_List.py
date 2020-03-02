def count_positives_sum_negatives(arr):
    if arr==[]:
        return []
    summ_pos = 0
    summ_neg = 0
    for i in arr:
        if i > 0:
            summ_pos +=1
        elif i < 0:
            summ_neg += i
    return [summ_pos, summ_neg]