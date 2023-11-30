from typing import List


class _1st:
    """
    正难则反
    先把所有数都选上（都加到答案中）
    然后考虑不选哪些点权

    dfs(x)
    对于一棵以x为根的子树，如果这棵树是健康的，损失的最小分数是多少

    选或不选
    损失根节点的情况下，损失的最小分数 =values[x]
    不损失根节点，损失的最小分数（根节点加到答案中去）= sum(dfs(y))
    这两种情况去min，作为dfs(x)的返回值

    递归边界：
    """

    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        g = [[] for _ in values]
        g[0].append(-1)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> int:
            if len(g[x]) == 1:
                return values[x] #递归到叶子节点，说明上面的节点全部加到ans中
            choose_loss = values[x]
            not_choose_loss = 0
            for y in g[x]:
                if y != fa:
                    not_choose_loss += dfs(y, x)
            return min(choose_loss, not_choose_loss)

        return sum(values) - dfs(0, -1)


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
        values = [20, 10, 9, 7, 4, 3, 5]
        handler.maximumScoreAfterOperations(edges,values)
