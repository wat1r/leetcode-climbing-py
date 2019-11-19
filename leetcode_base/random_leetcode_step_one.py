from typing import List


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    def test(self):
        amount = 10
        dp = [float("inf")] * (amount + 1)
        m = 3
        n = 4
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        return


if __name__ == '__main__':
    handler = RandomLeetcodeStepOne()
    # handler.init()
    # handler.minDistance()
    handler.test()
    handler.coinChange([1, 2, 5], 11)
