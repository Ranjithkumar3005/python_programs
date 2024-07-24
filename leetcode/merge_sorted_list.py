# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def toLinkedList(self, lst):
        """Helper function to convert a list into a linked list."""
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        linked_lists = [self.toLinkedList(lst) for lst in lists]
        dum=[]
        
        for i in range(0,len(lists)):
            head=linked_lists[i]
            while head:
                dum.append(head.val)
                head=head.next
        dum=sorted(dum)
                
        

s=Solution()
s.mergeKLists( lists = [[1,4,5],[1,3,4],[2,6]])