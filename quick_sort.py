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


'''
 * 快速排序
 *
 * 平均时间复杂度 - O(nlogn)
 * 最优时间复杂度 - O(nlogn)，每次选择的锚节点为中位数
 * 最差时间复杂度 - O(n^2)，每次选择的锚节点为最大/最小元素
 * 辅助空间 ------- 递归造成的栈空间使用，取决于树深度，一般为O(logn)，最差为O(n)
 * 稳定 ----------- 否
'''
if __name__ == '__main__':
    # initial disorder list
    nums = [num for num in range(1, 11)]
    random.shuffle(nums)
    print(nums) 
    # call function
    nums = quick_sort(nums)
    print(nums)
    