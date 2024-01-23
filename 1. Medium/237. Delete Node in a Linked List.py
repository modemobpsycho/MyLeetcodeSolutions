# Definition for singly-linked list.
from typing import Any


class ListNode:
    def __init__(self, x) -> None:
        self.val: Any = x
        self.next = None


class Solution:
    def deleteNode(self, node) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
