"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
        
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        count1 = 0
        count2 = 0
        while True:
            if l1 == None:
                break
            num1 += l1.val* 10 ** count1
            count1 += 1
            l1 = l1.next
        while True:
            if l2 == None:
                break
            num2 += l2.val * 10 ** count2
            l2 = l2.next
            count2 += 1
        sum_num = num1 + num2
        ret_node = ListNode(sum_num % 10)
        ret = ret_node
        sum_num = sum_num // 10
        while True:
            if sum_num == 0:
                break
            ret_node.next = ListNode(sum_num % 10)
            ret_node = ret_node.next
            sum_num = sum_num // 10
        return ret
                