"""
author: 汶穗
period: 19.11.23 - 19.12.06
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
    def contains(self, key):
        """
        :type key: int
        :rtype: bool(True or False)
        """
