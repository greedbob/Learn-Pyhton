# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        temp = ListNode(None)
        ans = temp
        while arr:
            temp.next = ListNode(None)
            temp = temp.next
            temp.val = arr.pop()
        return ans.next
