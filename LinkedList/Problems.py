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

def reorderList(head):
    # Step 1: Find the middle using fast & slow pointers
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Step 2: Split into two halves
    reverseHead = slow.next
    slow.next = None   # cut the list

    # Step 3: Reverse the second half
    prev = None
    while reverseHead:
        ahead = reverseHead.next
        reverseHead.next = prev
        prev = reverseHead
        reverseHead = ahead
    # now prev points to head of reversed second half

    # Step 4: Merge the two halves
    walker = head       # first half
    while walker and prev:
        ahead = walker.next      # save next from first half
        prevAhead = prev.next    # save next from second half

        walker.next = prev       # link node from first half → node from second half
        prev.next = ahead        # link node from second half → next of first half

        walker = ahead           # move forward in first half
        prev = prevAhead         # move forward in second half

    # Time complexity: O(n + n) => O(n)
    # Space complexity would be O(1).


def removeNthFromEnd(head, n):
    # First pass: get total length
    length = 0
    walker = head
    while walker:
        length += 1
        walker = walker.next

    # Edge case: removing head node
    if length - n == 0:
        return head.next

    # Second pass: find and remove target node
    walker = head
    prev = ListNode()  # Dummy node
    count = 0

    while walker:
        if length - count == n:  # Found nth from end
            prev.next = walker.next
            break

        prev = walker
        walker = walker.next
        count += 1

    # Time complexity: O(n) for iterating twice the list O(n + n) => O(n)
    # Space complexity: O(1) for just storing handful of variables.
    return head

def addTwoNumbers(l1, l2):
    # Dummy head to simplify result list creation
    newHead = ListNode()
    curr = newHead
    carry = 0
    # Continue while there are digits left in l1/l2 OR carry remains
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0   # digit from l1 (or 0 if None)
        v2 = l2.val if l2 else 0   # digit from l2 (or 0 if None)
        val = v1 + v2 + carry      # sum of both digits + carry

        carry = val // 10          # compute carry for next position
        val = val % 10             # current digit (0–9)

        # Append new digit node to result list
        node = ListNode(val)
        curr.next = node

        # Advance pointers
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        curr = curr.next

    # Return actual head (skip dummy)
    return newHead.next

def findDuplicate(nums):
    # Using HashMap for keeping the count of the numbers
    frequency = {}

    for n in nums:
        # Check if the number occurred before
        if n in frequency:
            return n

        frequency[n] = frequency.get(n, 0) + 1

    # Time complexity: O(n) for iterating over the array
    # Space Complexity: O(n) for keeping the HashMAP
    return -1

def copyRandomList(head):
    copies = {None: None}
    walker = head

    while walker:
        newNode = ListNode(walker.val)
        copies[walker] = newNode
        walker = walker.next

    walker = head
    while walker:
        curr = copies[walker]
        curr.random = copies[walker.random]
        curr.next = copies[walker.next]
        walker = walker.next

    return copies[head]


class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.val = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cache = {}  # hashmap: key -> node
        self.capacity = capacity
        self.head = self.Node(0, 0)  # dummy head
        self.tail = self.Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, node):
        # unlink node
        node.prev.next = node.next
        node.next.prev = node.prev
        # re-insert before tail
        self.add_to_tail(node)

    def add_to_tail(self, node):
        # insert node just before tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def removeLRU(self):
        # remove least recently used node (right after head)
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        # cleanup node
        node.prev = None
        node.next = None
        # delete from hashmap
        del self.cache[node.key]

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_tail(node)  # mark as recently used
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update value and move to tail
            node = self.cache[key]
            node.val = value
            self.move_to_tail(node)
        else:
            # create new node
            node = self.Node(key, value)
            self.cache[key] = node
            self.add_to_tail(node)

        if len(self.cache) > self.capacity:
            self.removeLRU()

