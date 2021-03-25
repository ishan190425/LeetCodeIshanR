def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
"""
This is a useful template for binary search
It saves time with having a condition of O(NLogN)
It does this by reducing half the length at each step
"""