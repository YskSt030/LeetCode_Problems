"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head        
        while head.val == val:
            head = head.next
            if head == None:
                return head
        node = head
        prev = None
        while True:
            if node == None:
                break
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head
                