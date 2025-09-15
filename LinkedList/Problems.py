# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

def reverseList(head):
    walker = head
    prev = None

    while walker:
        ahead = walker.next
        walker.next = prev
        prev = walker
        walker = ahead

    return prev


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists( list1, list2):
    head = ListNode()
    walker = head

    while list1 and list2:
        if list1.val < list2.val:
            walker.next = list1
            list1 = list1.next
        else:
            walker.next = list2
            list2 = list2.next

        walker = walker.next

    walker.next = list1 if list1 else list2

    return head.next