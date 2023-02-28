"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def unroll(self, x):
        out = []
        while x:
            out.append(x.val)
            x = x.next
        out = [str(k) for k in out[::-1]]
        return int("".join(out))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        v1, v2 = self.unroll(l1), self.unroll(l2)
        v0 = str(v1+v2)[::-1]
        cur = ans
        cur.val = v0[0]
        for n in v0[1:]:
            cur.next = ListNode(val=n)
            cur = cur.next
        return ans

"""
Linked List가 digit의 역순으로 정렬되어 있으므로 자릿수가 다를 가능성이 있어 cursor끼리 직접 더하면서 쌓아나가는 방식은 불가능하다.
결국 각각의 Linked list를 완전히 parse 한 뒤 더하고 이를 다시 linked list로 조립하는 접근을 취해야 한다.
아 내가 생각을 잘못했다. Head Node는 일의자리부터 시작하므로, 이렇게 unroll을 할 필요가 없고, 바로 one-by-one으로 덧셈을 하면서 올림만 신경써주면 된다.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        head = ListNode(0)
        cur = head
        while (l1 or l2 or c):
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            cur.next = ListNode(c%10)
            cur = cur.next
            c = c//10
        return head.next

"""
어차피 Linked-list는 일의자리-십의자리-... 순서로 구성되어 있으므로 pairwise로 덧셈을 하고 자릿수에 맞게 올림 처리를 해주면 된다.
그리고 head 자체를 반환하도록 할 경우 처음 시작 부분을 따로 코딩해줘야 하므로 사소하지만 이렇게 더미 노드로 시작해서 head.next를 return 하도록 하는 방식이 깔끔한 것 같다.
"""