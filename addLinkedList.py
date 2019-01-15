import json


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
        result = ListNode(0)
        head = result
        while(l1 or l2):
            if(l1 and l2):
                result.val=result.val + l1.val+l2.val
                l1=l1.next
                l2=l2.next
            elif(l1 and not l2):
                result.val=result.val + l1.val
                l1=l1.next
            elif(not l1 and  l2):
                result.val=result.val + l2.val
                l2=l2.next
            if(result.val>=10):
                result.val=result.val%10
                node= ListNode(1)
                result.next=node
                result=result.next
            elif(result.val<10):
                if(l1 or l2):
                    node = ListNode(0)
                    result.next=node
                    result=result.next
                    
        return head


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = "[2,4,3]"
            l1 = stringToListNode(line);
            line = "[5,6,4]"
            l2 = stringToListNode(line);

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
