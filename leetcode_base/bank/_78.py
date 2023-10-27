from typing import List


class _1st:
    print("")

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int):
            if i == n:
                ans.append(path.copy())
                return
            dfs(i + 1)  # 不选
            path.append(nums[i])  # 选
            dfs(i + 1)
            path.pop()  # 恢复现场

        dfs(0)
        return ans


class _2nd:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int):
            ans.append(path.copy())
            if i == n:
                return
            for j in range(i, n):
                path.append(nums[j])  # 选
                dfs(j + 1)
                path.pop()  # 恢复现场

        dfs(0)
        return ans


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    # handlers = [_2nd()]
    for handler in handlers:
        nums = [1, 2, 3]
        handler.subsets(nums)
