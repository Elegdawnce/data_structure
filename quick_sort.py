import numpy as np
import random

def helper(nums, left, right):
    if left >= right:
        return
    # choose left as pivot
    pivot = left
    # randomly select one pivot
    # pivot = nums.index(random.sample(nums[left:right+1],1)[0])
    
    # swap pivot with end
    nums[pivot], nums[right] = nums[right], nums[pivot]
    # num smaller than pivot
    small = left - 1
    # left pivot right
    for i in range(left, right):
        if nums[i] < nums[right]:
            small += 1
            if small != i:
                nums[i], nums[small] = nums[small], nums[i]
    
    # the position of pivot
    small += 1  
    # exchange again
    nums[small], nums[right] = nums[right], nums[small]
    # iteration
    helper(nums, left, small-1)
    helper(nums, small+1, right)


def quick_sort(nums):
    helper(nums, 0, len(nums)-1)
    return nums




if __name__ == '__main__':
    # initial disorder list
    nums = [num for num in range(1, 11)]
    random.shuffle(nums)
    print(nums) 
    # call function
    nums = quick_sort(nums)
    print(nums)