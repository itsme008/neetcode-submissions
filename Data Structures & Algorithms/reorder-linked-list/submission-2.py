# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_h = slow.next
        prev, slow.next = None, None

        while second_h:
            temp = second_h.next
            second_h.next = prev
            prev = second_h
            second_h = temp
            
        first_h, second_h = head, prev

        while second_h:
            tmp1, tmp2 = first_h.next, second_h.next
            first_h.next = second_h
            second_h.next = tmp1
            first_h, second_h = tmp1, tmp2
         

        