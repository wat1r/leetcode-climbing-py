import queue
from collections import deque
from typing import List


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class RandomLeetcodeStepOne():

    def init(self):
        return ""

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        def dp(i, j):
            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j - 1)) + 1

        return dp(len(word1) - 1, len(word2) - 1)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        return 1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, dp[i - c] + 1)
            dp[i] = cost
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None or right is None: return left == right
        if left.val != right.val: return False
        return self.check(left.right, right.left) and self.check(left.left, right.right)

    # recursive
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        self.visit_node(root, l)
        return l

    def visit_node(self, root, l):
        if root is None:
            return
        l.append(root.val)
        self.visit_node(root.left, l)
        self.visit_node(root.right, l)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        stack.append(root)
        res = []
        while stack:
            cur = stack.pop()
            if cur is None:
                continue
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder_visit_node(root, res)
        return res

    def inorder_visit_node(self, root, res):
        if root is None:
            return
        self.inorder_visit_node(root.left, res)
        res.append(root.val)
        self.inorder_visit_node(root.right, res)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur is None:
                continue
            stack.append(cur.left)
            stack.append(cur.right)
            res.append(cur.val)
        res.reverse()
        return res

    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root is None: return
    #     left = self.invertTree(root.left)
    #     right = self.invertTree(root.right)
    #     root.left = right
    #     root.right = left
    #     return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        from collections import deque
        if root is None: return
        queue = deque()
        queue.appendleft(root)
        while queue:
            cur = queue.pop()
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
            if cur.left: queue.appendleft(cur.left)
            if cur.right: queue.appendleft(cur.right)
        return root

    def HasSubtree(self, pRoot1, pRoot2):
        res = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val: res = self.HasSubtreeSegment(pRoot1, pRoot2)
            if res is False: res = self.HasSubtreeSegment(pRoot1.left, pRoot2)
            if res is False: res = self.HasSubtreeSegment(pRoot1.right, pRoot2)
        return res

    def HasSubtreeSegment(self, pRoot1, pRoot2) -> bool:
        if pRoot2 is None: return True
        if pRoot1 is None: return False
        if pRoot1.val != pRoot2.val: return False
        return self.HasSubtreeSegment(pRoot1.left, pRoot2) and self.HasSubtreeSegment(pRoot1.right, pRoot2)

    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     s = set()
    #     n = len(nums)
    #     for i in range(0, n):
    #         if nums[i] >= 1 and nums[i] <= n + 1:
    #             s.add(nums[i])
    #
    #     for i in range(1, n + 1):
    #         if i not in s:
    #             return i
    #     return n + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] >= 1 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        for i in range(n):
            if nums[i] != i + 1: return i + 1
        return n + 1

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

    def isValidBST(self, root: TreeNode) -> bool:

        """
        :param root:
        :return:
        """

        def helper(node, lower=float('-inf'), upper=float('+inf')):
            if not node: return True
            val = node.val
            if val <= lower or val >= upper: return False
            if not helper(node.left, lower, val): return False
            if not helper(node.right, val, upper): return False
            return True

        return helper(root)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def isValidBST(self, root: TreeNode) -> bool:
        stack, pre = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre >= root.val: return False
            pre = root.val
            root = root.right
        return True

    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next.next
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            if slow == fast: break
            slow = slow.next
            fast = fast.next.next
        if slow != fast: return None
        while head != slow.next:
            head = head.next
            slow = slow.next
        return head

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 if l1 else l2
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        node = dummy
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            # 注意将node移动向下一个
            node = node.next
        #     判断了不是null 节点
        node.next = l1 if l1 is not None else l2
        return dummy.next

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        record = dict()
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in record:
                res.append(i)
                res.append(record[remain])
                break
            record[nums[i]] = i
        return res

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        t = m + n + 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[t] = nums1[m]
                m -= 1
            else:
                nums1[t] = nums2[n]
                n -= 1
            t -= 1
        nums1[:n + 1] = nums2[:n + 1]

    def test(self):
        # amount = 10
        # dp = [float("inf")] * (amount + 1)
        # m = 3
        # n = 4
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        self.stack = []
        self.stack.append(1)
        self.stack.append(2)
        self.stack.append(3)
        self.stack.append(4)
        self.stack.append(5)

        return


if __name__ == '__main__':
    handler = RandomLeetcodeStepOne()
    # handler.init()
    # handler.minDistance()
    # handler.test()
    # handler.coinChange([1, 2, 5], 11)
    # node4 = TreeNode(4)
    # node2 = TreeNode(2)
    # node7 = TreeNode(7)
    # node4.left = node2
    # node4.right = node7
    # node1 = TreeNode(1)
    # node3 = TreeNode(3)
    # node6 = TreeNode(6)
    # node9 = TreeNode(9)
    #
    # node2.left = node1
    # node2.right = node3
    #
    # node7.left = node6
    # node7.right = node9
    #
    # handler.invertTree(node4)
    # handler.firstMissingPositive([1, 2, 0])
    # handler.firstMissingPositive([3, 4, -1, 1])
    # handler.firstMissingPositive([2])
    handler.firstMissingPositive([])
