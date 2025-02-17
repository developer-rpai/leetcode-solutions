def five_sort(nums):
    i = 0 
    j = len(nums) - 1

    while i <= j:
        if nums[i] == 5 and nums[j] != 5:
            nums[i], nums[j] = nums[j], nums[i]
             
            i += 1
            j -= 1
        elif nums[i] == 5 and nums[j] == 5:
            j -= 1
        else:
            i += 1
     

    return nums





nums = [5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]

print(five_sort(nums))