# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(head==None):
            return True
        if(head.next==None):
            return True
        count = 1
        temp=head
        while(temp.next!=None):
            temp=temp.next
            count = count +1
        half = int(count/2)
        i =1
        curr = head
        before = head
        odd =head
        while(i<=(count-half)):
            if(i==half):
                odd=curr
            before=curr
            curr=curr.next
            i=i+1
        before.next=None
        rev=self.reverse(curr)
        odd.next=None
        i=1
        while(i<=half):
            if(head.val!=rev.val):
                return False
            else:
                head=head.next
                rev=rev.next
                i=i+1
        return True
    def reverse(self,head):
        prev=None
        current=head.next
        while(current!=None):
            head.next = prev
            prev = head
            head= current
            current = current.next
        head.next=prev
        return head