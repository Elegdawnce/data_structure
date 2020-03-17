import numpy as np
import random
    

def shell_sort(nums):
    length = len(nums)
    step = int(length/2)
    while step > 0: # rounds
        for i in range(step, length): # every group
            # insert sort
            pivot = nums[i]
            j = i - step
            while j >= 0 and nums[j] > pivot:
                nums[j+step] = nums[j]
                j -= step
            nums[j+step] = pivot
        step = int(step/2)
    
    return nums



'''
 * 希尔排序
 *
 * 平均时间复杂度 - 根据步长序列的不同而不同，最好为O(n(logn)^2)
 * 最优时间复杂度 - O(n)
 * 最差时间复杂度 - 根据步长序列的不同而不同
 * 辅助空间 ------- O(1)
 * 稳定 ----------- 否
'''
if __name__ == '__main__':
    # initial disorder list
    nums = [num for num in range(1, 11)]
    random.shuffle(nums)
    print(nums) 
    # call function
    nums = shell_sort(nums)
    print(nums)
    