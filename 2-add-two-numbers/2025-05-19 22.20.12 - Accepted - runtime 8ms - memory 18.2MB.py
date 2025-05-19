# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_nodes(n1, n2, carry):
            if not n1 and not n2 and not carry:
                return None

            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            node = ListNode(total % 10)

            n1_next = n1.next if n1 else None
            n2_next = n2.next if n2 else None
            node.next = add_nodes(n1_next, n2_next, carry)
            return node

        return add_nodes(l1, l2, 0)
        
        