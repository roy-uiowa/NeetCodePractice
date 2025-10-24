"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyList = {None : None}

        cur = head
        while cur:
            copyNode = Node(cur.val)
            copyList[cur] = copyNode
            cur = cur.next

        cur = head
        while cur:
            copyList[cur].next = copyList[cur.next]
            copyList[cur].random = copyList[cur.random]
            cur = cur.next
        
        return copyList[head]

