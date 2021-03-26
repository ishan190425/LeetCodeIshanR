"""
Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
Example 4:

Input: s = "000"
Output: 0


Constraints:

s[i] == '0' or s[i] == '1'
1 <= s.length <= 10^5

This solution has a
Time Complex: O(N)
Space Complex: O(1)
"""


class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        old = 0
        for i in range(len(s)):
            if s[i] == '0':
                count = 0
            else:
                count += 1
            old += count
        return old % ((10 ** 9) + 7)
