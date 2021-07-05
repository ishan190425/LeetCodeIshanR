class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return self.helper(n // 2,1)
        else:
            return min(self.helper(n+1,1), self.helper(n-1,1))
        
    def helper(self,n, count):
        if n == 1:
            return count
        elif n % 2 == 0:
            return self.helper(n // 2, count + 1)
        else:
            return min(self.helper(n+1,count + 1), self.helper(n-1,count + 1))
        
