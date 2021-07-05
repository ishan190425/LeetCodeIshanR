class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        else: return self.helper(num, 0)
    def helper(self, num, count):
        num = num // 2 if num % 2 == 0 else num - 1
        if num == 0:
            return count + 1
        else:
            return self.helper(num, count + 1)
