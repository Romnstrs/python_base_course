def difference(*nums):
    if type(nums) == int or type(nums) == float:
        result = 0
    elif len(nums) == 0:
        result = 0
    else:
        result = max(nums) - min(nums)
    return result


print(difference(1,2,3,4,-2.2,5))

