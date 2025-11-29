# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        finalSum = ListNode() # Create first dummy node
        pointer = finalSum # Set pointer to point at the node

        carry = 0 # Counter to carry numbers
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # Set the number to its value unless there is none, then 0
            v2 = l2.val if l2 else 0

            digit = v1 + v2 + carry
            carry = digit // 10   # Divide by 10 to see if we have a number to carry
            value = digit % 10  # Get the remainder after division to get actual number

            pointer.next = ListNode(value) # Create new node after the one where the pointer is
            pointer = pointer.next # Pointer now points to new node

            l1 = l1.next if l1 else None # Move on to next number if possible
            l2 = l2.next if l2 else None
        return finalSum.next
