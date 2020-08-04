import numpy as np
import random
import copy

def helper(nums, left, right):
    if left >= right:
        return
    # choose mid
    mid = int((left + right) / 2)
    # iteration
    helper(nums, left, mid)
    helper(nums, mid+1, right)
    # combine 
    tmp = []
    i = left
    j = mid+1
    while i<= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    
    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= right:
        tmp.append(nums[j])
        j += 1
    # Assignment
    for i in range(len(tmp)):
        nums[left+i] = tmp[i]


def merge_sort(nums):
    helper(nums, 0, len(nums)-1)
    return nums


'''
 * 归并排序
 *
 * 平均时间复杂度 - O(nlogn)
 * 最优时间复杂度 - O(nlogn)
 * 最差时间复杂度 - O(nlogn)
 * 辅助空间 ------- O(n)
 * 稳定 ----------- 是
'''
if __name__ == '__main__':
    # initial disorder list
    nums = [num for num in range(1, 11)]
    random.shuffle(nums)
    print(nums) 
    # call function
    nums = merge_sort(nums)
    print(nums)
    
