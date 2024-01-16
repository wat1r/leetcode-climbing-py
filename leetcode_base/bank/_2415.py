from typing import List, Optional

from leetcode_base.random_leetcode_step_one import TreeNode


class _1st:
    # 该二叉树是完美二叉树
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(l: Optional[TreeNode], r: Optional[TreeNode], isOdd: bool) -> None:
            if l is None:
                return
            if isOdd:
                l.val, r.val = r.val, l.val
            dfs(l.left, r.right, not isOdd)
            dfs(r.left, l.right, not isOdd)

        dfs(root.left, root.right, True)
        return root


class _2nd:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        isOdd = False
        while len(q) > 0:
            if isOdd:
                for i in range(len(q) // 2):
                    nodex, nodey = q[i], q[len(q) - 1 - i]
                    nodex.val, nodey.val = nodey.val, nodex.val
            tmp = q
            q = []
            for node in tmp:
                if node.left is not None:
                    q.append(node.left)
                    q.append(node.right)
            isOdd ^= True
        return root


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print()
