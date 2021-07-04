class Solution:
    def findMin(self, nums: List[int]) -> int:
        high = len(nums) - 1
        h = nums[high]
        if high == 0:
            return nums[0]
        low = 0
        l = nums[low]
        while high >= low:
            hl = nums[high-1]
            if h < hl:
                return h
            lh = nums[low+1]
            if l > lh:
                return lh
            else:
                low += 1
                high -= 1
                l = lh
                h = hl
        return nums[0]
