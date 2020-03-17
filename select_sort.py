import numpy as np
import random



def select_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    
    return nums



'''
 * 选择排序
 *
 * 平均时间复杂度 - O(n^2)
 * 最优时间复杂度 - O(n^2)
 * 最差时间复杂度 - O(n^2)
 * 辅助空间 ------- O(1)
 * 稳定 ----------- 否
 * [5*, 8, 5, 2, 9]
 * [2, 8, 5, 5*, 9]
'''
if __name__ == '__main__':
    # initial disorder list
    nums = [num for num in range(1, 11)]
    random.shuffle(nums)
    print(nums) 
    # call function
    nums = select_sort(nums)
    print(nums)
    
