import numpy as np
import random

# big heap
def helper(nums, pos):
    # left child : 2*pos + 1
    left = pos * 2 + 1
    # right child : 2*pos + 2
    right = left + 1
    # big heap
    max = pos
    # if left child > parent : update
    if left < len(nums) and nums[left] > nums[max]:
        max = left

    # if right child > parent : update
    if right < len(nums) and nums[right] > nums[max]:
        max = right

    if max != pos:
        nums[pos], nums[max] = nums[max], nums[pos]
        helper(nums, max)
    

def heap_sort(nums):
    # create the big heap
    for i in range(int(len(nums)/2), -1, -1):
        helper(nums, i)

    length = len(nums)
    # every round, put root to the end, and resort 
    for i in range(len(nums)-1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        tmp = nums[:i]
        helper(tmp, 0)
        for j in range(len(tmp)):
            nums[j] = tmp[j]
            
    return nums



'''
 * 堆排序
 *
 * 平均时间复杂度 - O(nlogn)
 * 最优时间复杂度 - O(nlogn)
 * 最差时间复杂度 - O(nlogn)
 * 辅助空间 ------- O(1)
 * 稳定 ----------- 否
'''
if __name__ == '__main__':
    # initial disorder list
    nums = [num for num in range(1, 11)]
    random.shuffle(nums)
    print(nums) 
    # call function
    nums = heap_sort(nums)
    print(nums)
    