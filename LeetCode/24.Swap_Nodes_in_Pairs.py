# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ans = p = ListNode(None)
        ans.next = head
        while head and head.next:
            sec = head.next  # sec记录第二个
            head.next = head.next.next  # 第一个指向第三个
            
            sec.next = head  # 第二个指向第一个
            p.next = sec  # 使ans指向反转后的第一个
            
            p = head  # p指向反转后的第二个
            head = head.next
        return ans.next

    def swapPairs_recursion(self, head: ListNode) -> ListNode:
        ans = p = ListNode(None)
        ans.next = head
        if not head or not head.next:
            return head
        else:
            temp = head.next
            head.next = self.swapPairs(head.next.next)
            temp.next = head
            return temp