from typing import List, Optional

from leetcode_base.random_leetcode_step_one import TreeNode


class _1st:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode):
            if root is None:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            f = [0, 0]
            f[0] = max(left[0], left[1]) + max(right[0], right[1])
            f[1] = root.val + left[0] + right[0]
            return f

        return max(dfs(root))


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
