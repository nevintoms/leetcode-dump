'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''

# Solution 1:
def findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    op = sum(nums[:k])
    top=op
    for i in range(1, len(nums)-k+1):
        temp=0
        op = op - nums[i-1] + nums[i+k-1]
        if op > top:
            top = op
    return float(top)/k

# Solution 2(best):
def findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    win = sum(nums[:k])
    maxSum = win
    for i in range(len(nums)-k):
        win = win - nums[i] + nums[i+k]
        if win>maxSum:
            maxSum = win
    return maxSum/float(k)

