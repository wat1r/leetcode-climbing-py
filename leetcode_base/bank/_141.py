from leetcode_base.struct.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next: return False
            slow = slow.next
            fast = fast.next.next
        return True


if __name__ == '__main__':
    l0 = ListNode(3)
    l1 = ListNode(2)
    l2 = ListNode(0)
    l3 = ListNode(-4)
    l0.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l1
    handler = Solution()
    handler.hasCycle(l0)
