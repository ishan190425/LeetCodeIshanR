# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        x = []
        for i in range(len(lists)):
            z = lists[i]
            while(z != None):
                x.append(z.val)
                z = z.next
        x.sort()
        if x is None or len(x) == 0:
            return None
        l = ListNode(x[0])
        z = l
        for i in range(1, len(x)):
            l.next = ListNode(x[i])
            l = l.next
        return z
