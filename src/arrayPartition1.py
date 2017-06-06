class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Test
        list.sort(nums)
        print(nums)
        my_len = len(nums)
        i = 0
        sum = 0 
        
        
        while i < my_len:
            sum += nums[i]
            i += 2;

        return sum;

