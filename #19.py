"""
2023.03.14
"""
"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dumm = ListNode()
        dumm.next = head
        cur, sur = dumm, dumm
        for _ in range(n+1):
            sur = sur.next
        while sur:
            cur = cur.next
            sur = sur.next
        cur.next = cur.next.next
        return dumm.next

"""
Send a survey unit (n+1) step ahead, so that if we come across None, we know that it's time to replace cur.next with cur.next.next (skip the next one).
Time > 70.22%, Memory > 57.67%
"""