#!/usr/bin/python3
def is_palindrome(head):
    """
    Check if a singly linked list is a palindrome.
    :param head: Head node of the linked list
    :return: True if the linked list is a palindrome, False otherwise
    """
    if not head:
        return True

    # Get the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Reverse the first half of the linked list
    mid = length // 2
    prev = None
    current = head
    for i in range(mid):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # If the length of the linked list is odd, skip the middle node
    if length % 2 != 0:
        current = current.next

    # Compare the reversed first half with the second half
    while prev and current:
        if prev.val != current.val:
            return False
        prev = prev.next
        current = current.next

    return True

