from random import randint

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.orignal = tuple(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = list(self.orignal)
        return self.orignal
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.nums)):
            temp = random.randint(0,len(self.nums)-1)
            t = self.nums[i]
            self.nums[i] = self.nums[temp]
            self.nums[temp] = t
        return self.nums
            
        
