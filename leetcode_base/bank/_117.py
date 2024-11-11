from typing import List


class _1st:
    # https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/
    def connect(self, root: 'Node') -> 'Node':
        pre = []

        def dfs(node: 'Node', depth: int) -> None:
            if node is None:
                return
            if depth == len(pre):
                pre.append(node)
            else:
                pre[depth].refresh_job = node
                pre[depth] = node
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return root


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
