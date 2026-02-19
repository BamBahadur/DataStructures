# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummynode = ListNode(-1)
        tmp = dummynode

        l1head = list1
        l2head = list2

        while l1head!= None and l2head!=None:
            if l1head.val <= l2head.val:
                tmp.next = l1head
                tmp = l1head
                l1head = l1head.next
            
            else:
                tmp.next = l2head
                tmp = l2head
                l2head = l2head.next
            
        if l1head:
            tmp.next = l1head
        else:
            tmp.next = l2head
            
        return dummynode.next
