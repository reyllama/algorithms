"""
2023.03.17
"""
"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dumm = ListNode()
        cur0, cur1, cur2 = dumm, list1, list2
        while cur1 or cur2:
            if not cur2:
                cur0.next = cur1
                cur0 = cur0.next
                cur1 = cur1.next
            elif not cur1:
                cur0.next = cur2
                cur0 = cur0.next
                cur2 = cur2.next
            else:
                if cur1.val > cur2.val:
                    cur0.next = cur2
                    cur0 = cur0.next
                    cur2 = cur2.next
                else:
                    cur0.next = cur1
                    cur0 = cur0.next
                    cur1 = cur1.next
        return dumm.next

"""
Have three pointers, each for list1, list2 and our answer.
Move them accordingly, comparing the existence and values.
Time > 90.90%, Memory > 67.32%
"""