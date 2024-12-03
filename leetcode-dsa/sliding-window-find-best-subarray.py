def find_best_subarray(nums, k):
    
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i+k]
        max_sum = max(max_sum, window_sum)
    return max_sum




nums = [3,1, 4,12,8,15,6]
k = 4

print(find_best_subarray(nums,k))
