import json


class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if (l1.val <= l2.val):
            head = l1
            self.merge(l1, l2)
            return head
        else:
            head = l2
            self.merge(l2, l1)
            return head

    def merge(self, l1, l2):
        if (l1.next == None):
            if (l2 == None):
                return True
            else:
                l1.next = l2
                return True
        else:
            if (l2 == None):
                return True
            else:
                if (l2.val < l1.next.val):
                    big = l1.next
                    l1.next = l2
                    l2 = l2.next
                    l1 = l1.next
                    l1.next = big
                    self.merge(l1, l2)
                else:
                    l1 = l1.next
                    self.merge(l1, l2)


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
            line = "[-9,3]"
            l1 = stringToListNode(line);
            line = "[5,7]"
            l2 = stringToListNode(line);

            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()