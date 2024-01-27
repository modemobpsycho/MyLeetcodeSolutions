# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0

        while head:
            ans: int = ans * 2 + head.val
            head = head.next

        return ans
