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


def insert_sort(nums):
    for i in range(1, len(nums)):
        pivot = nums[i]
        j = i-1
        flag = False
        while j >= 0:
            if pivot < nums[j]:
                nums[j+1] = nums[j]
            else:
                nums[j+1] = pivot
                flag = True
                break
            j -= 1
        if flag == False:
            nums[j+1] = pivot
    return nums



'''
 * 直接插入排序
 *
 * 平均时间复杂度 - O(n^2)
 * 最优时间复杂度 - O(n)，升序情况
 * 最差时间复杂度 - O(n^2)，降序情况
 * 辅助空间 ------- O(1)
 * 稳定 ----------- 是
'''
if __name__ == '__main__':
    # initial disorder list
    nums = [num for num in range(1, 11)]
    random.shuffle(nums)
    print(nums) 
    # call function
    nums = insert_sort(nums)
    print(nums)
    