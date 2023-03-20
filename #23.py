"""
2023.03.20
"""
"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Make the code concise
        def rearrange(c1, c2):
            c1.next = c2
            c1 = c1.next
            c2 = c2.next
            return c1, c2

        # Merge two sorted linked-lists
        def mergeTwo(head1, head2):
            head0 = ListNode()
            cur0, cur1, cur2 = head0, head1, head2
            while cur1 or cur2:
                if not cur2:
                    cur0, cur1 = rearrange(cur0, cur1)
                elif not cur1:
                    cur0, cur2 = rearrange(cur0, cur2)
                else:
                    if cur1.val < cur2.val:
                        cur0, cur1 = rearrange(cur0, cur1)
                    else:
                        cur0, cur2 = rearrange(cur0, cur2)
            return head0.next

        # Group every one or two linked lists and merge them bottm up (round-robin)
        if len(lists)==0:
            return
        if len(lists)==1:
            return lists[0]
        elif len(lists)==2:
            return mergeTwo(lists[0], lists[1])
        return mergeTwo(self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:]))


"""
Time > 27.25%, Memory > 89.72
"""

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def rearrange(c1, c2):
            c1.next = c2
            c1 = c1.next
            c2 = c2.next
            return c1, c2

        def mergeTwo(head1, head2):
            head0 = ListNode()
            cur0, cur1, cur2 = head0, head1, head2
            while cur1 or cur2:
                if not cur2:
                    cur0, cur1 = rearrange(cur0, cur1)
                elif not cur1:
                    cur0, cur2 = rearrange(cur0, cur2)
                else:
                    if cur1.val < cur2.val:
                        cur0, cur1 = rearrange(cur0, cur1)
                    else:
                        cur0, cur2 = rearrange(cur0, cur2)
            return head0.next

        if len(lists) == 0:
            return
        ans = lists.pop()
        while lists:
            ans = mergeTwo(ans, lists.pop())

        return ans


"""
Worst Case Scenario: O((mk)^2)
"""