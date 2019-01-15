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
        head = l1
        addhead = l2
        curr = head
        add = addhead
        l1num = 0
        l2num = 0
        while (add != None):
            l2num = l2num + 1
            if (curr == None):
                break;
            l1num = l1num + 1
            curr = curr.next
            add = add.next
        if (l1num < l2num):
            head = l2
            addhead = l1
        curr = head
        add = addhead
        while (curr != None):
            if (add != None):
                curr.val = curr.val + add.val
                add = add.next
            if (curr.val >= 10):
                curr.val = curr.val%10
                if (curr.next == None):
                    node = ListNode(1)
                    curr.next = node
                else:
                    curr.next.val = curr.next.val + 1
            curr = curr.next
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