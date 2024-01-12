def increasingTriplet(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import math
        i = j = k = float('inf')

        for x in nums:
            if x < i:
                i = x
            if x < j and x>i:
                j = x
            if x < k and x>i and x>j:
                return True
        return False

print(increasingTriplet([2,1,5,0,4,6]))