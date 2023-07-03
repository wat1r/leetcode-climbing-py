from cmath import inf
from typing import Optional

from leetcode_base.random_leetcode_step_one import TreeNode


class _1st:

    def __init__(self) -> None:
        self.res = -inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode):
            if root is None:
                return 0
            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)
            self.res = max(self.res, root.val + l + r)
            return root.val + max(l, r)

        dfs(root)
        return self.res


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        handler.maxPathSum([1, 2, 3])
