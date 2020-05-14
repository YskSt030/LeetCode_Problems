# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_head = head
        node_top = head
        node_tail = head
        for i in range(n):
          print('i:{}'.format(i))
          if node_head.next == None and i == n - 2:
            return node_tail.next
          node_head = node_head.next
        while True:
            node_head = node_head.next
            node_tail = node_tail.next
            if node_head.next == None:
                node_tail.next = node_tail.next.next
                break
                
        return node_top
        
    def setNode(self, list):
    	head = ListNode(list[0])
    	node = head
    	for i in range(1, len(list)):
    		node.next = ListNode(list[i])
    		node = node.next
    
    def showNode(self, head: ListNode):
    	while head.next != None:
    		print('{},'.format(head.val))
    		head = head.next	
    		
if __name__ == '__main__':
	sol = Solution()
	list = [1, 2, 3]
	head = sol.setNode(list)
	sol.showNode(head)
	ret = sol.removeNthFromEnd(list, 2)
	sol.showNode(ret)
	
	
    		
    	
