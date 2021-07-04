class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = 0
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] = d.get(nums[i]) + 1
            else:
                d[nums[i]] = 1
        for i in range(len(nums)):
            current = nums[i]
            comp = k - current
            if comp in d:
                if comp == current:
                    c += d[comp] // 2
                    d[comp] = 0
                else:
                    c += min(d[comp], d[current])
                    d[comp] = 0
                    d[current] = 0
        return c
