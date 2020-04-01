# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val > l2.val:
            temp = l1
            l1 = l2
            l2 = temp
        ans = l1
        while l1 and l2:
            if l1.next is None:
                l1.next = l2
                break
            elif l1.next.val > l2.val:
                temp = l1.next
                l1.next = ListNode(l2.val)
                l1.next.next = temp
                l2 = l2.next
            l1 = l1.next
        return ans
    
    def mergeTwoLists_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        head = ans
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return ans.next

    # recursion version
    def mergeTwoLists_recursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        head = ListNode(None)
        if l1.val < l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head= l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head
