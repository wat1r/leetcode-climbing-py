from typing import List, Optional

from leetcode_base.random_leetcode_step_one import TreeNode


class _1st:
    def rob(self, root: Optional[TreeNode]) -> int:
        # [not_choose,choose,]表示不选/选当前节点，以当前节点为根的子树的最大点权和
        def dfs(root: TreeNode) -> (int, int):
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
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0, 0
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)
            rob = l_not_rob + r_not_rob + node.val
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            return rob, not_rob

        return max(dfs(root))


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
