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