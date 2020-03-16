import numpy as np
import random


def helper(nums, left, right, target):
    # fail to find target
    if left > right:
        return -1
    
    mid = int((left + right) / 2)
    # find target and return the pos
    if target == nums[mid]:
        return mid
    # find target in left list
    elif target < nums[mid]:
        return helper(nums, left, mid-1, target)
    # find target in right list
    elif target > nums[mid]:
        return helper(nums, mid+1, right, target)

def binary_search(nums, target):
    return helper(nums, 0, len(nums)-1, target)


'''
 * 二分查找
 *
 * 平均时间复杂度 - O(logn)
 * 最优时间复杂度 - O(1)，target为中位数
 * 最差时间复杂度 - O(logn)，查找失败
 * 辅助空间 ------- 递归造成的栈空间使用，取决于树深度，一般为O(logn)，最差为O(n)
'''
if __name__ == '__main__':
    # initial disorder list
    nums = [num for num in range(1, 11)]
    print("nums: ", nums) 
    # call function
    target = random.sample(nums, 1)[0]
    print("target: ", target)
    pos = binary_search(nums, target)
    if pos == -1:
        print("Not found!")
    else:
        print("pos:", pos)
    