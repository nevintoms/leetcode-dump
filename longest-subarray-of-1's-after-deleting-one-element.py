'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
'''

# Solution 1:
def longestSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if list(set(nums))[0] == 1:
        return len(nums)-1
    
    l = r = cnt = max_cnt = 0
    k = 1
    while(r < len(nums)):
        if nums[r] == 0:
            if k==0:
                max_cnt = max(max_cnt, cnt)
                if nums[l] == 0:
                    k+=1
                else:
                    cnt-=1
                l+=1
            else:
                k-=1
                r+=1
        else:
            r+=1
            cnt+=1
    max_cnt = max(max_cnt, cnt)
    return max_cnt