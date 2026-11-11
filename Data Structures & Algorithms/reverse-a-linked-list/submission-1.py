# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            # 1. 先保存下一个节点，避免后面的链表丢失
            next_node = current.next

            # 2. 反转当前节点的箭头
            current.next = prev

            # 3. prev 向前移动到当前节点
            prev = current

            # 4. current 移动到原来的下一个节点
            current = next_node
        return prev
