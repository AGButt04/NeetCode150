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

