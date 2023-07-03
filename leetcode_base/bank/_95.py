from typing import List, Optional

from leetcode_base.random_leetcode_step_one import TreeNode


class _1st:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start: int, end: int):
            if start > end:
                return [None]
            total = []
            for i in range(start, end + 1):
                left_tree = dfs(start, i - 1)
                right_tree = dfs(i + 1, end)
                for l in left_tree:
                    for r in right_tree:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        total.append(cur)
            return total

        return dfs(1, n) if n else []


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
