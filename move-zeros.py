'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
'''

# This question can be thought of moving zeros to the end or moving non zeros to the begining. 
# Later would be the best approach.

# Solution 1: Moving zeros to the end
def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 1
    while((i < len(nums)-1) & (j < len(nums))):
        if nums[i] == 0:
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        else:
            i+=1
        j+=1
    return nums


