import json

class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if (head == None):
            return head
        if (head.next == None):
            return head
        if (n == m):
            return head
        i = 1
        start = False
        realhead = head
        if (i == m):
            start = True
        while (i < m):
            begin = head
            head = head.next
            i = i + 1
        prev = None
        current = head.next
        end = head
        while (i <= n):
            if (current == None):
                head.next = prev
                if(not start):
                    begin.next = head
                    return realhead
                break;
            head.next = prev
            prev = head
            head = current
            current = current.next
            i = i + 1
        if (start):
            if(i<=n):
                return head
            end.next=head
            return prev
        end.next = head
        begin.next = prev
        return realhead


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
            line = "[1,2,3]"
            head = stringToListNode(line);
            line = 2
            m = int(line);
            line = 3
            n = int(line);

            ret = Solution().reverseBetween(head, m, n)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
