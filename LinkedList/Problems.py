# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.

def hasCycle(head):
    # Floyd's Tortoise and Hare algorithm
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # move 1 step
        fast = fast.next.next     # move 2 steps

        if slow == fast:          # cycle detected
            return True

    # Time: O(n) — each pointer visits at most n nodes
    # Space: O(1) — only two pointers used

    return False                  # no cycle

def reverseList(head):
    # Iteratively reverse linked list
    walker = head
    prev = None

    while walker:
        ahead = walker.next       # save next node
        walker.next = prev        # reverse pointer
        prev = walker             # move prev forward
        walker = ahead            # move walker forward

    # Time: O(n) — each node processed once
    # Space: O(1) — only a few pointers

    return prev                   # new head of reversed list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    # Merge two sorted linked lists into one sorted list
    head = ListNode()             # dummy head
    walker = head

    while list1 and list2:
        if list1.val < list2.val:
            walker.next = list1
            list1 = list1.next
        else:
            walker.next = list2
            list2 = list2.next

        walker = walker.next      # move forward

    walker.next = list1 if list1 else list2  # attach remainder

    # Time: O(n + m) — n = len(list1), m = len(list2)
    # Space: O(1) — only extra dummy node/pointer

    return head.next              # skip dummy
