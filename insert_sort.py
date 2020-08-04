import numpy as np
import random



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


def insert_sort(nums):
    for i in range(1, len(nums)):
        left = 0
        right = i-1
        flag = 0
        while left < right:
            mid = (left+right)//2
            if nums[mid] == nums[i]:
                pos = i
                flag = 1
                break
            elif nums[mid] > nums[i]:
                right = mid
            else:
                left = mid + 1
        if flag == 0:
            pos = left
        nums = nums[:pos] + [nums[i]] + nums[pos:i] + nums[i+1:]
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
    
