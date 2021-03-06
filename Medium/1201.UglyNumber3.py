"""
Given four integers n, a, b, and c, return the nth ugly number.

Ugly numbers are positive integers that are divisible by a, b, or c.



Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984


Constraints:

1 <= n, a, b, c <= 109
1 <= a * b * c <= 1018
It is guaranteed that the result will be in range [1, 2 * 109].

This Solution has a:
Time Complex : O(NLogN)
Space ComplexL O(1)
"""
from math import gcd
class Solution:
    def lcm(self, x, y):
        return (x * y) // (gcd(x, y))

    def count_ugly(self, n, a, b, c, ab, bc, ca, abc):
        answer = (n // a) + (n // b) + (n // c)
        answer -= (n // ab) + (n // bc) + (n // ca)
        answer += (n // abc)
        return answer

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab, bc, ca = self.lcm(a, b), self.lcm(b, c), self.lcm(c, a)
        abc = self.lcm(ab, c)
        low = 1
        high = 2 * 10 ** 9  # constraint
        while low < high:
            mid = low + ((high - low) // 2)
            count = self.count_ugly(mid, a, b, c, ab, bc, ca, abc)
            if count < n:
                low = mid + 1
            else:
                high = mid
        return low
