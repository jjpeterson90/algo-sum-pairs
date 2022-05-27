def sum_pairs(int_arr, desired_sum):
    result = []
    for i in range(len(int_arr)):
        for j in range(i+1, len(int_arr)):
            if int_arr[i] + int_arr[j] == desired_sum :
                result.append([int_arr[i], int_arr[j]])
    if len(result) == 0:
        return 'unable to find pairs'
    if len(result) == 1:
        return result[0]
    else:
        return result

#print(sum_pairs([1,2,3,4,5], 9))                          # [[4,5]]
#print(sum_pairs([1,2,3,4,5], 7))                 # [[2,5], [3,4]]
#print(sum_pairs([3, 1, 5, 8, 2], 27)) 